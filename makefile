# Makefile for structure_and_landscapes

# Uses gcc for compiling
CC=gcc
LD=gcc

# Flags for compiling (mostly needed for Vienna RNA and cython)
CFLAGS=-shared -fopenmp -pthread -fPIC -fwrapv -O2 -Wall -fno-strict-aliasing -I/usr/include/python -I/usr/local/include/ViennaRNA
LFLAGS=-L/usr/local/lib/ViennaRNA -lRNA 

# Not real targets
.PHONY: test coverage run install style profile clean clean_cython analysis cython_compile all

# Default target; runs all 'not slow' tests (excludes integration tests)
test: all
	nosetests -a '!slow' -- 

# Runs all tests (including integration tests)
test-all: all
	nosetests --

# Default target to be (currently 'test' to ease testing)
all: cython_compile

# Tells us unittesting line coverage 
coverage: clean cython_compile
	nosetests --with-coverage --

# Installs the needed dependancies
install:
	pip install nose coverage pep8 cython RunSnakeRun

# Runs pep8 (python style checker) on all .py file
style:
	find . -name \*.py | xargs pep8

# Removes compilation product (should be just source surviving)
clean: clean_cython
	-find . -name \*.pyc | xargs rm 
	-rm profiledata
	-rm -r .coverage

# Visual profiler
profile: .profiledata 
	runsnake $<


# Cleans cython specific files
clean_cython:
	-rm rna/vienna_distance.c
	-rm rna/*.o
	-rm rna/*.so

# Cython complied libraries 
cython_compile: rna/vienna_distance.so

rna/vienna_distance.so: rna/vienna_distance.c rna/vienna_utils.o
	$(CC) $(CFLAGS) -o $@ rna/vienna_distance.c rna/vienna_utils.o $(LFLAGS)
	
rna/vienna_distance.c: rna/vienna_distance.pyx
	cython rna/vienna_distance.pyx -o $@

rna/vienna_utils.o: rna/vienna_utils.c rna/vienna_utils.h
	$(CC) $(CFLAGS) -c rna/vienna_utils.c -o $@ $(LFLAGS)

.profiledata: main.py
	python -m cProfile -o $@ main.py
