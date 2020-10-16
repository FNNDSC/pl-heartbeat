pl-heartbeat
===============

.. image:: https://badge.fury.io/py/heartbeat.svg
    :target: https://badge.fury.io/py/heartbeat

.. image:: https://travis-ci.org/FNNDSC/heartbeat.svg?branch=master
    :target: https://travis-ci.org/FNNDSC/pl-heartbeat

.. image:: https://img.shields.io/badge/python-3.5%2B-blue.svg
    :target: https://badge.fury.io/py/heartbeat

.. contents:: Table of Contents


Abstract
--------

``heartbeat`` is a simple app that periodically displays system information.

Synopsis
--------

.. code::

    python heartbeat.py                                             \
        [-v <level>] [--verbosity <level>]                          \
        [--infoType <typeSystemInfo>]                               \
        [--beatInterval <secondsWait>]                              \
        [--lifetime <secondsLive>]                                  \
        [--version]                                                 \
        [--man]                                                     \
        [--meta]                                                    \
        /tmp



Run
----

This ``plugin`` can be run in two modes: natively as a python package or as a containerized docker image.

Using PyPI
~~~~~~~~~~

To run from PyPI, simply do a

.. code:: bash

    pip install heartbeat

and run with

.. code:: bash

    heartbeat.py --beatInterval 5 --lifetime 50 /tmp

to specify system information to be displayed, simply do

.. code:: bash

    heartbeat.py --infoType CPU         \
                 --beatInterval 5       \
                 --lifetime 50          \
                      /tmp


Using ``docker run``
~~~~~~~~~~~~~~~~~~~~

To run using ``docker``, prefix all calls with

.. code:: bash

    docker run --rm                                     \
        fnndsc/pl-heartbeat heartbeat.py


Examples
--------

Display DateTime Information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

    docker run --rm                                     \
        fnndsc/pl-heartbeat heartbeat.py                \
        --infoType datetime                             \
        /tmp


Display CPU Information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

    docker run --rm                                     \
        fnndsc/pl-heartbeat heartbeat.py                \
        --infoType cpu                                  \
        /tmp

Display Memory Information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

    docker run --rm                                     \
        fnndsc/pl-heartbeat heartbeat.py                \
        --infoType memory                               \
        /tmp

Display System Information every 15 seconds for 1 minute
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

    docker run --rm                                     \
        fnndsc/pl-heartbeat heartbeat.py                \
        --infoType datetime                             \
        --beatInterval 15                               \
         --lifetime 60                                  \
        /tmp