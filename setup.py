from os import path

from setuptools import find_packages, setup
from torch.utils.cpp_extension import BuildExtension, CppExtension

here = path.abspath(path.dirname(__file__))
with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="cornerpool",
    version="0.0.2",
    description="Cornerpooling in pytorch",
    long_description=long_description,
    author="Bishwarup Bhattacharjee",
    author_email="write2bishwarup@gmail.com",
    python_requires=">=3.6",
    packages=find_packages(),
    ext_modules=[
        CppExtension("cornerpool.libs.top_pool", ["./cornerpool/src/top_pool.cpp"]),
        CppExtension(
            "cornerpool.libs.bottom_pool", ["./cornerpool/src/bottom_pool.cpp"]
        ),
        CppExtension("cornerpool.libs.left_pool", ["./cornerpool/src/left_pool.cpp"]),
        CppExtension("cornerpool.libs.right_pool", ["./cornerpool/src/right_pool.cpp"]),
    ],
    cmdclass={"build_ext": BuildExtension},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    license="MIT",
    url="https://github.com/bishwarup307/cornerpool",
)
