#!/usr/bin/env bash

/opt/apache/spark-2.1.1/bin/spark-submit --driver-memory 8g --conf "spark.scheduler.listenerbus.eventqueue.size=30000" --conf "spark.shuffle.service.enabled=False" --conf "spark.sql.shuffle.partitions=2048" --conf "spark.driver.maxResultSize=3g" /home/qin/weekly_keyword_count/run.py >> /home/qin/weekly_keyword_count/kwd_count.log 2>&1
