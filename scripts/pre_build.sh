yum -y update && yum -y install wget
echo "installed wget"

# python3 -m 
# echo "installed pytorch"

wget https://download.pytorch.org/libtorch/cpu/libtorch-shared-with-deps-1.7.1%2Bcpu.zip
echo "downloaded pytorch c++ libraries"

unzip libtorch-shared-with-deps-1.7.1+cpu -d /opt

# export LD_LIBRARY_PATH="/opt/libtorch/lib${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"
