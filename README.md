# Cornerpool

![Build](https://github.com/bishwarup307/cornerpool/workflows/Build/badge.svg)

Cornerpool is a small python utility for *corner pooling* as originally introducted in the [CornerNet paper](https://arxiv.org/abs/1808.01244)

## Installation

You must have `torch>=1.6.0` installed before installing `cornerpool`

```sh
conda create -n cornerpool python=3.8 pip
pip install torch
```
Once you have pytorch installed, install `cornerpool` with:

```sh
pip install cornerpool
```

## Usage:
```python
>>> import torch
>>> from cornerpool import TopPool, LeftPool, RightPool, BottomPool

>>> a = torch.randint(low=0, high=5, size=(1, 2, 4, 4))
>>> print(a)
tensor([[[[2, 1, 2, 2],
          [3, 4, 1, 3],
          [2, 2, 0, 1],
          [4, 2, 4, 0]],

         [[2, 3, 0, 0],
          [3, 4, 0, 1],
          [0, 0, 2, 3],
          [2, 3, 3, 3]]]])

>>> tp = TopPool()
>>> print(tp(a))
tensor([[[[4, 4, 4, 3],
          [4, 4, 4, 3],
          [4, 2, 4, 1],
          [4, 2, 4, 0]],

         [[3, 4, 3, 3],
          [3, 4, 3, 3],
          [2, 3, 3, 3],
          [2, 3, 3, 3]]]])
```