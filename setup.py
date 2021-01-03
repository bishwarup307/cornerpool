from setuptools import setup, find_packages
from torch.utils.cpp_extension import BuildExtension, CppExtension

setup(
    name="cornerpool",
    version="0.0.1",
    packages=find_packages(),
    ext_modules=[
        CppExtension("top_pool", ["./cornerpool/src/top_pool.cpp"]),
        CppExtension("bottom_pool", ["./cornerpool/src/bottom_pool.cpp"]),
        CppExtension("left_pool", ["./cornerpool/src/left_pool.cpp"]),
        CppExtension("right_pool", ["./cornerpool/src/right_pool.cpp"]),
    ],
    cmdclass={"build_ext": BuildExtension},
)
