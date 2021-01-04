yum -y update && yum -y install wget
echo "installed wget"

pip install torch==1.7.1+cpu -f https://download.pytorch.org/whl/torch_stable
echo "installed pytorch"

wget https://download.pytorch.org/libtorch/cpu/libtorch-shared-with-deps-1.7.1%2Bcpu.zip
echo "downloaded pytorch c++ libraries"

unzip libtorch-shared-with-deps-1.7.1+cpu -d /opt

export LD_LIBRARY_PATH="/opt/libtorch/lib${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"
