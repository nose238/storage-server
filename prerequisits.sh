# It is needed that this dir (storage-server) has 755 permises
# Installing C and C++ compiler
yum install gcc gcc-c++ autoconf automake;
# Downloading Jailkit
yum install wget;
wget https://olivier.sessink.nl/jailkit/jailkit-2.20.tar.gz;
# Extracting files
tar -vzxf jailkit-2.20.tar.gz;
# Installing Jailkit
cd jailkit-2.20;
./configure;
make;
make install;