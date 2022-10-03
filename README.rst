pl-statsmodels
================================

.. image:: https://img.shields.io/docker/v/fnndsc/pl-statsmodels?sort=semver
    :target: https://hub.docker.com/r/fnndsc/pl-statsmodels

.. image:: https://img.shields.io/github/license/fnndsc/pl-statsmodels
    :target: https://github.com/FNNDSC/pl-statsmodels/blob/master/LICENSE

.. image:: https://github.com/FNNDSC/pl-statsmodels/workflows/ci/badge.svg
    :target: https://github.com/FNNDSC/pl-statsmodels/actions


.. contents:: Table of Contents


Abstract
--------

An application that fit OLS model on the inputs and present results in output.
Idea users of this tool includes doctors, healthcare professionals or anyone familiar with the ChRIS project


Description
-----------


``statsmodels_tool`` is a *ChRIS ds-type* application that takes in images as  files
and produces text.


Usage
-----

.. code::

    docker run --rm fnndsc/pl-statsmodels statsmodels_tool
        [-h|--help]
        [--json] [--man] [--meta]
        [--savejson <DIR>]
        [-v|--verbosity <level>]
        [--version]
        [--columns] <columnsForOLS>
        <inputDir> <outputDir>


Arguments
~~~~~~~~~

.. code::

    [-h] [--help]
    If specified, show help message and exit.
    
    [--json]
    If specified, show json representation of app and exit.
    
    [--man]
    If specified, print (this) man page and exit.

    [--meta]
    If specified, print plugin meta data and exit.
    
    [--savejson <DIR>] 
    If specified, save json representation file to DIR and exit. 
    
    [-v <level>] [--verbosity <level>]
    Verbosity level for app. Not used currently.
    
    [--version]
    If specified, print version number and exit. 

    [--columns]
    [REQUIRED] Columns to be used as input for OLS. Refer: https://www.statsmodels.org/devel/gettingstarted.html for more information.


Getting inline help is:

.. code:: bash

    docker run --rm fnndsc/pl-statsmodels statsmodels_tool --man

Run
~~~

You need to specify input and output directories using the `-v` flag to `docker run`.


.. code:: bash

    docker run --rm -u $(id -u)                                             \
        -v $(pwd)/test_input:/incoming -v $(pwd)/test_output:/outgoing      \
        fnndsc/pl-statsmodels statsmodels_tool                              \
        --columns "Lottery ~ Literacy + Wealth + Region"                    \
        /incoming /outgoing


Development
-----------

Build the Docker container:

.. code:: bash

    docker build --tag pl-statsmodels -f ./Dockerfile

Run unit tests:

.. code:: bash

    docker run --rm pl-statsmodels nosetests

Examples
--------

Running docker container:

.. code:: bash

    docker run --rm -u $(id -u) -v $(pwd)/test_input:/incoming -v $(pwd)/test_output:/outgoing local/pl-statsmodels statsmodels_tool --columns "Lottery ~ Literacy + Wealth + Region" /incoming /outgoing

.. image:: https://raw.githubusercontent.com/FNNDSC/cookiecutter-chrisapp/master/doc/assets/badge/light.png
    :target: https://chrisstore.co
