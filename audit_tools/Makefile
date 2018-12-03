#
# Makefile for audit_tools
# =============================================================================
#


.DEFAULT: help
.PHONY: help
help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  clean       to remove all build, test, coverage and Python artifacts"
	@echo "  clean-build to remove all build artifacts"
	@echo "  clean-pyc   to remove all Python artifacts"
	@echo "  clean-test  to remove all test artifacts"
	@echo "  init        to setup pipenv and install dependencies"
	@echo "  lint        to check style with pylint"
	@echo "  test        to run tests"
	@echo "  docs        to generate Sphinx documentation"
	@echo "  build-sdist to build a source distribution"
	@echo "  build-wheel to build a binary wheel distribution"
	@echo "  build       to build all distributions"
	@echo "  install     to install the package to Python's site-packages"


# Remove all build, test, coverage and Python artifacts
.PHONY: clean
clean: clean-build clean-pyc clean-test


# Remove all build artifacts
.PHONY: clean-build
clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +


# Remove all Python artifacts
.PHONY: clean-pyc
clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +


# Remove all test artifacts
.PHONY: clean-test
clean-test:
	rm -fr .cache/


# Setup pipenv and install dependencies
.PHONY: init
init:
	pip install pipenv
	pipenv install -e .
	pipenv lock
	pipenv install --dev


# Check style with pylint
.PHONY: lint
lint:
	pipenv run flake8 audit_tools tests


# Run tests
.PHONY: test
test:
	pipenv run py.test


# Generate Sphinx HTML documentation, including API docs
.PHONY: docs
docs:
	rm -f docs/audit_tools.rst
	rm -f docs/modules.rst
	pipenv run sphinx-apidoc -o docs/ audit_tools
	$(MAKE) -C docs clean
	$(MAKE) -C docs html


# Build source distribution
.PHONY: clean build-sdist
build-sdist:
	pipenv run python setup.py sdist


# Build binary wheel distribution
.PHONY: clean build-wheel
build-wheel:
	pipenv run python setup.py bdist_wheel


# Build all distributions
.PHONY: build
build: build-sdist build-wheel


# Install the package to site-packages
.PHONY: install
install: clean
	pipenv run python setup.py install
