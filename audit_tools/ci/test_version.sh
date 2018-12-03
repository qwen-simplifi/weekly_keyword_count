#!/usr/bin/env bash

# Tests to ensure the version of the package aligns with what we push to Artifactory
#
# This should catch instances were a version bump was missed, or a release was incorrectly tagged


# These tests don't apply if we're on the develop branch, so we just bypass them here.
[ "${TRAVIS_BRANCH}" = 'develop' ] && exit 0

# Identify the version of the package
PKG_VER="$(pipenv run python -c 'from audit_tools import __version__; print(__version__)')"

if [ "${TRAVIS_TAG}" = "" ]
then
  echo -e "Testing that an existing git tag does not exist for this version of audit_tools..."

  if git ls-remote --tags origin | grep 'refs/tags/$${PKG_VER}}'; then
    echo -e "\033[1;31mTag for this version already exists!\033[m"
    echo -e "\033[0;31mDid you forget to bump the version?\033[m"
	exit 1
  else
    echo -e "\033[1;32mTag for this version does not exist.\033[m"
  fi

else
  echo -e "Testing that the git tag matches the version of audit_tools..."

  echo -e "Package Version: ${PKG_VER}"
  echo -e "Git Tag Version: ${TRAVIS_TAG}"

  if [[ "${PKG_VER}" == "${TRAVIS_TAG}" ]]
  then
     echo -e "\033[1;31mVersions Match!\033[m"
  else
     echo -e "\033[1;32mVersion Mismatch!\033[m"
     exit 1
  fi

fi
