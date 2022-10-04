# A ChRIS statsmodels plugin app

[![Version](https://img.shields.io/docker/v/fnndsc/pl-statsmodels?sort=semver)](https://hub.docker.com/r/fnndsc/pl-statsmodels)
[![MIT License](https://img.shields.io/github/license/fnndsc/pl-statsmodels)](https://github.com/FNNDSC/pl-statsmodels/blob/main/LICENSE)
[![ci](https://github.com/FNNDSC/pl-statsmodels/actions/workflows/ci.yml/badge.svg)](https://github.com/FNNDSC/pl-statsmodels/actions/workflows/ci.yml)

`pl-statsmodels` is a [_ChRIS_](https://chrisproject.org/)
_ds_ plugin which takes in CSV data as input files and
creates result summary of Ordinary Least Square fit as output files.

## Abstract

An application that takes CSV files as input and fits an OLS model on it. The result summary of the OLS fit is stored in output folder.

## Installation

`pl-statsmodels` is a _[ChRIS](https://chrisproject.org/) plugin_, meaning it can
run from either within _ChRIS_ or the command-line.

[![Get it from chrisstore.co](https://ipfs.babymri.org/ipfs/QmaQM9dUAYFjLVn3PpNTrpbKVavvSTxNLE5BocRCW1UoXG/light.png)](https://chrisstore.co/plugin/pl-statsmodels)

## Local Usage

1. Building container image using `podman`/`docker`:

```shell
docker build --tag pl-statsmodels -f ./Dockerfile
```

2. Add the CSV file on which the OLS models has to be fitted. [Reference](https://www.statsmodels.org/devel/gettingstarted.html)  
3. Executing container image 

```shell
docker run --rm -u $(id -u) -v $(pwd)/test_input:/incoming -v $(pwd)/test_output:/outgoing local/pl-statsmodels statsmodels_tool --columns "Lottery ~ Literacy + Wealth + Region" /incoming /outgoing
```
**NOTE**: `--columns` is a required (string) parameter for the `statsmodels_tool` utility

### Testing

```shell
docker run --rm pl-statsmodels nosetests
```

## Release

Steps for release can be automated by [Github Actions](.github/workflows/ci.yml).
This section is about how to do those steps manually.

### Increase Version Number

Increase the version number in `setup.py` and commit this file.

### Push Container Image

Build and push an image tagged by the version. For example, for version `1.2.3`:

```
docker build -t docker.io/fnndsc/pl-statsmodels:1.2.3 .
docker push docker.io/fnndsc/pl-statsmodels:1.2.3
```

### Get JSON Representation

Run [`chris_plugin_info`](https://github.com/FNNDSC/chris_plugin#usage)
to produce a JSON description of this plugin, which can be uploaded to a _ChRIS Store_.

```shell
docker run --rm localhost/fnndsc/pl-statsmodels:dev chris_plugin_info > chris_plugin_info.json
```

