"""
题目描述
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。
请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
比如n=3时，2*3的矩形块有3种覆盖方法：
"""
# 小矩形是2*1，它可以横着放或这竖着放，共两种形式。
# 当大矩形2*n，考虑现在状态由前一状态转化而来。
# 若现在横着放，则由f(n-2)方法，若竖着放，则有f(n-1)种方法，所以共有f(n-1) + f(n-2)种方法


def rectCover( number):
    # write code here
    if number <= 2:
        return number
    i, j = 1, 2
    while number > 1:
        i, j = j, i + j
        number -= 1
    return i