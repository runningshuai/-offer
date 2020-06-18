"""
请实现一个函数，将一个字符串中的每个空格替换成“%20”。
例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
"""
# 时间换空间做法，在原来字符串上修改，不开辟新的空间
# 字符串的增加：尾部增加 + ，中间增加要转换成list
# 字符的删除，也是转成list
# 改，通过replace
# 查，index
# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        s = s.replace(' ', '%20')
        return s


s = "hello world"
s = s.replace(' ', '20%')
print(s)