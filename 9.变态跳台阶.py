"""
题目描述
一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。
求该青蛙跳上一个n级的台阶总共有多少种跳法。
"""
# f(n) = f(n-1) + f(n-2) + ... + f(1) ①
# f(n-1) = f(n-2) + ... + f(1) ②
# ①-②，f(n) = 2*f(n-1)

def jumpFloorII(self, number):
    # write code here
    # 2**(number-1)
    # 快速幂
    n = number - 1
    res = 1
    base = 2
    while n:
        if n & 1:
            res *= base
        base *= base
        n = n >> 1
    return res