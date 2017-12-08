from sifi_spark_support import sifi_spark_base as sss
from sifi_spark_support.Connections.sifi_vertica import SifiVertica
from pyspark.sql import functions as f

other = dict([("spark.master", "spark://dcspark5-int:7077"),
              ("spark.scheduler.listenerbus.eventqueue.size", "30000"),
              ("spark.shuffle.service.enabled", "false"),
              ("spark.sql.shuffle.partitions", "2048"),
              ("spark.driver.maxResultSize", "3g")])


def main():
    sc, sqlc = sss.setup_spark_with_sql(memory="31g",
                                        prefix="AdOps Keyword Count",
                                        other=other)

    sifi_day_today = sss.get_sifi_date()
    # daily keyword count, for different data sources
    parquet_kw_estimates = 'hdfs://dchdpname1-int:8020/parquet/kw_modeling/kw_estimates_by_data_source/sifi_date={0:d}'
    df_parquet = sqlc.read.parquet(parquet_kw_estimates.format(sifi_day_today))
    df_count_ordered = df_parquet.filter(f.col('data_source') == 'bidder_path_keywords')\
        .filter(f.col('count') > 2)\
        .orderBy(f.col('count').desc())\
        .cache()
    df_count_ordered.count()

    # keyword md5 and names
    parquet_kw_index = 'hdfs://dchdpname1-int:8020/parquet/kw_modeling/kw_index_by_week/sifi_date={0:d}'
    df_kw = sqlc.read.parquet(parquet_kw_index.format(sifi_day_today))\
        .filter(f.length(f.col('segment_name')) < 30).cache()
    df_kw.count()

    # Add the keyword names
    df_count_ordered_with_name = df_count_ordered.join(df_kw, 'md5', 'inner')\
        .orderBy(f.col('count').desc())\
        .limit(10000000)\
        .select(f.col('count').alias('keyword_count'),
                f.col('md5'),
                f.col('segment_name').alias('keyword_name')).cache()
    df_count_ordered_with_name.count()
    # add dd_id
    df_final = df_count_ordered_with_name.withColumn('dd_id', f.lit(sifi_day_today))\
        .select(f.col('dd_id'), f.col('keyword_count'), f.col('keyword_name'), f.col('md5'))

    # Write to Vertica
    SifiVertica(sqlc=sqlc, environment="prod").write_dataframe(df_final.coalesce(8), "top_keywords", schema="adops")

    sc.stop()


if __name__ == '__main__':
    main()
