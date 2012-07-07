CC=gcc
LD=gcc

CFLAGS=-shared -fopenmp -pthread -fPIC -fwrapv -O2 -Wall -fno-strict-aliasing -I/usr/include/python2.7 -I/usr/local/include/ViennaRNA

LFLAGS=-L/usr/local/lib/ViennaRNA -lRNA 

.PHONY: test coverage run install style profile clean clean_cython analysis

test: vienna_distance.so
	nosetests --

coverage: vienna_distance.so
	nosetests --with-coverage --

run: vienna_distance.so
	python2.7 main.py

install: vienna_distance.so
	pip install nose coverage pep8 cython RunSnakeRun

style:
	pep8 *.py

clean: clean_cython
	rm *.pyc *.o *.so profiledata
	rm -r .coverage

analysis:
	pip install numpy 
	pip install matplotlib

vienna_distance.so: vienna_distance.c vienna_utils.o
	$(CC) $(CFLAGS) -o $@ vienna_distance.c vienna_utils.o $(LFLAGS)
	
vienna_distance.c: vienna_distance.pyx
	cython vienna_distance.pyx

clean_cython:
	rm vienna_distance.c

vienna_utils.o: vienna_utils.c vienna_utils.h
	$(CC) $(CFLAGS) -c vienna_utils.c -o $@ $(LFLAGS)

profile: .profiledata 
	runsnake $<

.profiledata: main.py
	python -m cProfile -o $@ main.py
