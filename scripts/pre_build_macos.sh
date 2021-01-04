wget -q wget https://download.pytorch.org/libtorch/cpu/libtorch-macos-1.7.1.zip
unzip -qq libtorch-macos-1.7.1.zip -d $GITHUB_WORKSPACE
rm -f libtorch-macos-1.7.1.zip