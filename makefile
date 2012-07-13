CC=gcc
LD=gcc

CFLAGS=-shared -fopenmp -pthread -fPIC -fwrapv -O2 -Wall -fno-strict-aliasing -I/usr/include/python2.7 -I/usr/local/include/ViennaRNA
LFLAGS=-L/usr/local/lib/ViennaRNA -lRNA 

.PHONY: test coverage run install style profile clean clean_cython analysis cython_compile all

test: all
	nosetests --

all: clean cython_compile

coverage: clean cython_compile
	nosetests --with-coverage --

run: clean cython_compile
	python2.7 main.py

install: 
	pip install nose coverage pep8 cython RunSnakeRun

style:
	pep8 *.py

clean: clean_cython
	-find . -name \*.pyc | xargs rm 
	-rm profiledata
	-rm -r .coverage

clean_cython:
	-rm rna/vienna_distance.c
	-rm rna/*.o
	-rm rna/*.so

analysis:
	pip install numpy 
	pip install matplotlib

cython_compile: rna/vienna_distance.so

rna/vienna_distance.so: rna/vienna_distance.c rna/vienna_utils.o
	$(CC) $(CFLAGS) -o $@ rna/vienna_distance.c rna/vienna_utils.o $(LFLAGS)
	
rna/vienna_distance.c: rna/vienna_distance.pyx
	cython rna/vienna_distance.pyx -o $@

rna/vienna_utils.o: rna/vienna_utils.c rna/vienna_utils.h
	$(CC) $(CFLAGS) -c rna/vienna_utils.c -o $@ $(LFLAGS)

profile: .profiledata 
	runsnake $<

.profiledata: main.py
	python -m cProfile -o $@ main.py
