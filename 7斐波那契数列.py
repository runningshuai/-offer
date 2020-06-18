# -*- coding:utf-8 -*-
"""
题目描述
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0，第1项是1）。
n<=39
"""
import time
# 递归，开销很大
def Fibonacci(n):
    # write code here
    if n == 0:
        return 0
    if n == 1:
        return 1
    return Fibonacci(n - 1) + Fibonacci(n - 2)


# 用两个变量保存之前的数
def Fibonacci2(n):
    i, j = 0, 1
    while n:
        i, j = j, i + j
        n -= 1
    return i


# 快速幂
# 常数的快速幂, python 十进制可以直接右yi
def fast_pow(base, n):
    res = 1
    while n:
        if n&1 == 1:
            res *= base
        base *= base
        n = n >> 1
    return res


# 矩阵快速幂，要实现矩阵的乘法
def matrix_multi(A, B):
    if not A or not B:
        return None
    m, n = len(A), len(A[0])
    p, q = len(B), len(B[0])
    # 不满足矩阵相乘的时候
    if n != p:
        return None
    # 结果是m*q的
    result = []
    for _ in range(m):
        result.append([0]*q)
    # 矩阵相乘
    for i in range(m):
        for j in range(q):
            temp = 0
            for t in range(n):
                temp += A[i][t] * B[t][j]
            result[i][j] = temp
    return result


# 矩阵的n-1次幂，左上角的元素
def Fibonacci3(n):
    base = [[1, 1], [1, 0]]
    result = [[1, 0], [0, 1]]
    n = n - 1
    while n:
        if n&1 == 1:
            result = matrix_multi(result, base)
        base = matrix_multi(base, base)
        n = n >> 1
    return result[0][0]

num = 800000
a = time.time()

res = Fibonacci2(num)
b = time.time()
print(b - a)
c = time.time()
res = Fibonacci3(num)
d = time.time()
print(d-c)
