mkdir ~/glibc_install; cd ~/glibc_install 
wget http://ftp.gnu.org/gnu/glibc/glibc-2.14.tar.gz
tar zxvf glibc-2.14.tar.gz
cd glibc-2.14

mkdir build
cd build

../configure --prefix=/opt/glibc-2.14

make -j4

sudo make install

export LD_LIBRARY_PATH="/opt/glibc-2.14/lib${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"
pip install torch