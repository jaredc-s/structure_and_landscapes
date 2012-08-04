apt-get -y update
apt-get -y dist-upgrade
apt-get -y install make git python-numpy build-essential python2.7-dev python-pip vim
wget http://www.tbi.univie.ac.at/~ronny/RNA/ViennaRNA-2.0.7.tar.gz
tar -xf ViennaRNA-2.0.7.tar.gz
cd ViennaRNA-2.0.7
./configure
make
make install
cd ~
cd structure_and_landscapes
make install
