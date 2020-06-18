"""
题目描述
将一个字符串转换成一个整数，要求不能使用字符串转换整数的库函数。 数值为0或者字符串不是一个合法的数值则返回0
输入描述:
输入一个字符串,包括数字字母符号,可以为空
输出描述:
如果是合法的数值表达则返回该数字，否则返回0
题目理解：
把数字字符串转化成整数
"""
class Solution:
    def StrToInt(self, s):
        # write code here
        if not s:
            return 0
        if s[0] == '0':
            return 0
        result = 0
        length = len(s)
        flag = 1
        legal = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-']
        for i in range(length):
            if s[i] in legal:
                if s[i] == '+':
                    flag = 1
                    continue
                if s[i] == '-':
                    flag = -1
                    continue
                result = result*10 + legal.index(s[i])
            else:
                return 0
        return flag*result


