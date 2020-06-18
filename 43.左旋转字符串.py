"""
题目描述
汇编语言中有一种移位指令叫做循环左移（ROL），现在有个简单的任务，就是用字符串模拟这个指令的运算结果。
对于一个给定的字符序列S，请你把其循环左移K位后的序列输出。
例如，字符序列S=”abcXYZdef”,要求输出循环左移3位后的结果，即“XYZdefabc”。是不是很简单？OK，搞定它！
"""
class Solution1:
    def LeftRotateString(self, s, n):
        # write code here
        # 把旋转次数n，处理成单周期内
        if not s:
            return ''
        n = n % len(s)
        s1 = s[:n]
        s2 = s[n:]
        return s2 + s1

class Solution2:
    def LeftRotateString(self, s, n):
        # write code here
        # 删除，添加到最后
        if not s:
            return ''
        n = n % len(s)
        lis = list(s)
        for i in range(n):
            lis.append(lis.pop(0))
        return ''.join(lis)
