"""
给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
保证base和exponent不同时为0
"""


# 快速幂解法，要考虑分母为0的情况
def Power(base, exponent):
    # write code here
    res = 1
    n = exponent
    if exponent < 0:
        n = abs(exponent)
    while n:
        if n & 1:
            res *= base
        base *= base
        n = n >> 1
    if exponent < 0:
        res = 1 / res
    return res