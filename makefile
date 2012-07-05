test: vienna_distance.so
	nosetests --

coverage: vienna_distance.so
	nosetests --with-coverage --

run: vienna_distance.so
	python2.7 main.py

install: vienna_distance.so
	pip install nose coverage pep8 cython

style:
	pep8 *.py

clean: clean_cython
	rm *.pyc *.o *.so

analysis:
	pip install numpy 
	pip install matplotlib

vienna_distance.so: vienna_distance.c vienna_utils.o
	gcc -shared -fopenmp -pthread -fPIC -fwrapv -O2 -Wall -fno-strict-aliasing -I/usr/include/python2.7 -o vienna_distance.so vienna_distance.c vienna_utils.o -L /usr/local/lib/ViennaRNA -lRNA 

vienna_distance.c: vienna_distance.pyx
	cython vienna_distance.pyx

clean_cython:
	rm vienna_distance.c

vienna_utils.o: vienna_utils.c vienna_utils.h
	gcc -c -fopenmp vienna_utils.c -I /usr/local/include/ViennaRNA
