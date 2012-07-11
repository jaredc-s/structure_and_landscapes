========================
Structure and Landscapes
========================

Description
===========
This Python project investigates the effect population structure has on 
organisms with smooth or rugged adaptive landscapes. Various sequence to
fitness mappings will be explored including:

* RNA secondary structure
* Simple Integer Model 
* Bitstrings
* Kauffman's N-K Model

Authors
=======
* `Jared Carlson-Stevermer`_
* `Joshua Nahum`_ 
* `Joseph Marcus`_
.. _`Jared Carlson-Stevermer` : jmcs@utexas.edu
.. _`Joseph Marcus` : josephhmarcus@gmail.com 
.. _`Joshua Nahum` : josh@nahum.us

Requirements
============

Mandatory
+++++++++
* Python 2.7

Optional
++++++++
* Ned Batchelder's coverage.py
* Nose
* Pep8
* Numpy
* Matplotlib

Install
=======
1)github: https://github.com/jhmarcus/structure-and-landscapes
2)downloads https://github.com/jhmarcus/structure-and-landscapes/downloads
3)download as zip using the defult archive manager
4)sudo apt-get install python2.7-dev
    - version python2.7-dev (2.7.3-0ubuntu3)
5)sudo apt-get install build-essential
    - version build-essential (11.5ubuntu2)
6)sudo apt-get install pep8
7) pep8 's version (0.6.1-2ubuntu2)
8) sudo apt-get install python-pip
9) pip version (1.0-1build1)

Runsnakerun
+++++++++++
http://www.vrplumber.com/programming/runsnakerun/

depedencies for runsnakerun
apt-get install python-profiler python-wxgtk2.8 python-setuptools

ViennaRNA
+++++++++
http://www.tbi.univie.ac.at/~ivo/RNA/
http://www.tbi.univie.ac.at/~ronny/RNA/vrna2_source.html

follow instructions on install
./configure
make
sudo make install

version 2.0.7
download source code and use the default archive manager!

Add this package to PYTHONPATH
++++++++++++++++++++++++++++++
Add this line to ~/.bashrc::

export PYTHONPATH=$PYTHONPATH:$PATH_TO_DIRECTORY_CONTAINING_structure_and_landscape
