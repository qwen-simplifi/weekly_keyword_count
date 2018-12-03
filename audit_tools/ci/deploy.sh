#!/usr/bin/env bash

PKG_VER="$(pipenv run python -c 'from audit_tools import __version__; print(__version__)')"

# Install JFrog CLI (if its not already there)
if [ ! -f  ~/.cache/jfrog ]; then
  echo "Downloading JFrog CLI..."
  mkdir -p ~/.cache
  curl -fL https://api.bintray.com/content/jfrog/jfrog-cli-go/\$latest/jfrog-cli-linux-amd64/jfrog?bt_package=jfrog-cli-linux-amd64 --output ~/.cache/jfrog
  chmod +x ~/.cache/jfrog
else
  echo "Using cached JFrog CLI..."
fi

echo "Logging into Artifactory as ${DEPLOY_USER}..."
~/.cache/jfrog rt config \
  --url=https://artifact.simpli.fi/artifactory \
  --user=${DEPLOY_USER} \
  --password=${DEPLOY_PW} \
  audit_tools

echo "Uploading audit_tools v${PKG_VER} distributions to Artifactory..."
~/.cache/jfrog rt upload \
  --props="pypi.name=audit_tools;pypi.version=${PKG_VER}" \
  --build-name="${TRAVIS_BUILD_ID}" \
  --build-number=${TRAVIS_BUILD_NUMBER} \
  "./dist/audit_tools-*" \
  pypi/audit_tools/${PKG_VER}/
