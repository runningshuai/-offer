"""
题目描述
写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。
思路：
①不考虑进位：两个数之和是异或
②计算进位：求与，左移一位
若②不为0，就继续①②步
"""
class Solution:
    def Add(self, num1, num2):
        # write code here
        if not num1:
            return num2
        elif not num2:
            return num1
        while num2:
            num1, num2 = (num1 ^ num2) & 0xFFFFFFFF, (num1 & num2) << 1

        if num1 >> 31 == 0:
            return num1
        else:
            return num1 - 2**32


if __name__ == '__main__':
    s = Solution()
    print(s.Add(-1, 1))
