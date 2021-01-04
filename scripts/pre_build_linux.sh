yum -y update && yum -y install wget
echo "installed wget"

# python3 -m 
# echo "installed pytorch"

wget -q https://download.pytorch.org/libtorch/cpu/libtorch-shared-with-deps-1.7.1%2Bcpu.zip
echo "downloaded pytorch c++ libraries"

unzip -qq libtorch-shared-with-deps-1.7.1+cpu.zip -d /opt
rm -f libtorch-shared-with-deps-1.7.1+cpu.zip
# export LD_LIBRARY_PATH="/opt/libtorch/lib${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"
