===============================
audit_tools
===============================

.. image:: https://img.shields.io/travis/simplifi/audit_tools.svg
        :target: https://travis-ci.com/simplfifi/audit_tools


Data Quality Audit Tools


Development
-----------

This project uses the following worklow tools/methodologies:
- `PipEnv`_: For development dependencies and virtual environments
- `git-flow`_: For branching


To initialize your development environment run `make init`.

If you'd like to see all the options available you can simply run `make` to
see the list.

.. _PipEnv: https://docs.pipenv.org/
.. _git-flow: https://danielkummer.github.io/git-flow-cheatsheet/


Deployment
----------

When you are confident your changes are ready, push your branch up to GitHub
and submit a pull request against the appropriate branch (varies depending on
branching strategy). This will trigger a build in TravisCI.

**You may not merge your changes until the tests have passed and someone has
approved your pull request.**

Once a version is tagged in git, TravisCI will build and push the package to
Simplifi's Artifactory.

There should be no need to manually push a package to Artifactory.
**Please do not do this.**


Usage
-----

To use this package you'll need to tell pip how to find our Artifactory repo.
This can be accomplished in one of two ways...

Add the index to `~/.pip/pip.conf` file:
.. code-block::
    [global]
    index-url = https://artifact.int.simpli.fi/artifactory/api/pypi/pypi/simple

Or add the index to the `requirements.txt` file for your project:
.. code-block::
    --index-url https://artifact.int.simpli.fi/artifactory/api/pypi/pypi/simple
    pytest==3.3.2
    pylint==1.7.2

You should now be able to install this package via pip.


Features
--------

* TODO
