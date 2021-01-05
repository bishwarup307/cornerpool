from torch import nn
from torch.autograd import Function

# from .libs import bottom_pool, right_pool, left_pool, top_pool
# from cornerpool import libs
import cornerpool.libs.top_pool
import cornerpool.libs.bottom_pool
import cornerpool.libs.right_pool
import cornerpool.libs.left_pool


__all__ = ["TopPool", "BottomPool", "LeftPool", "RightPool"]


class TopPoolFunction(Function):
    @staticmethod
    def forward(ctx, input):
        output = cornerpool.libs.top_pool.forward(input)[0]
        ctx.save_for_backward(input)
        return output

    @staticmethod
    def backward(ctx, grad_output):
        input = ctx.saved_variables[0]
        output = cornerpool.libs.top_pool.backward(input, grad_output)[0]
        return output


class BottomPoolFunction(Function):
    @staticmethod
    def forward(ctx, input):
        output = cornerpool.libs.bottom_pool.forward(input)[0]
        ctx.save_for_backward(input)
        return output

    @staticmethod
    def backward(ctx, grad_output):
        input = ctx.saved_variables[0]
        output = cornerpool.libs.bottom_pool.backward(input, grad_output)[0]
        return output


class LeftPoolFunction(Function):
    @staticmethod
    def forward(ctx, input):
        output = cornerpool.libs.left_pool.forward(input)[0]
        ctx.save_for_backward(input)
        return output

    @staticmethod
    def backward(ctx, grad_output):
        input = ctx.saved_variables[0]
        output = cornerpool.libs.left_pool.backward(input, grad_output)[0]
        return output


class RightPoolFunction(Function):
    @staticmethod
    def forward(ctx, input):
        output = cornerpool.libs.right_pool.forward(input)[0]
        ctx.save_for_backward(input)
        return output

    @staticmethod
    def backward(ctx, grad_output):
        input = ctx.saved_variables[0]
        output = cornerpool.libs.right_pool.backward(input, grad_output)[0]
        return output


class TopPool(nn.Module):
    def forward(self, x):
        return TopPoolFunction.apply(x)


class BottomPool(nn.Module):
    def forward(self, x):
        return BottomPoolFunction.apply(x)


class LeftPool(nn.Module):
    def forward(self, x):
        return LeftPoolFunction.apply(x)


class RightPool(nn.Module):
    def forward(self, x):
        return RightPoolFunction.apply(x)
