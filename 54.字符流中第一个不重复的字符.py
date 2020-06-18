"""
题目描述
请实现一个函数用来找出字符流中第一个只出现一次的字符。例如，当从字符流中只读出前两个字符"go"时，
第一个只出现一次的字符是"g"。当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。
输出描述:
如果当前字符流没有存在出现一次的字符，返回#字符。
解法：
利用一个int型数组表示256个字符，这个数组初值置为-1.
每读出一个字符，将该字符的位置存入字符对应数组下标中。
若值为-1标识第一次读入，不为-1且>0表示不是第一次读入，将值改为-2.
之后在数组中找到>0的最小值，该数组下标对应的字符为所求。
在python中，ord(char)是得到char对应的ASCII码；chr(idx)是得到ASCII位idx的字符
链接：https://www.nowcoder.com/questionTerminal/00de97733b8e4f97a3fb5c680ee10720
来源：牛客网
"""
class Solution:
    # 返回对应char
    def __init__(self):
        self.arr = [-1] * 256
        self.index = 0

    def FirstAppearingOnce(self):
        # write code here
        min = 256
        index = -1
        # 找值最小的元素,并记录索引
        for i in range(256):
            if 0 <= self.arr[i] < min:
                min = self.arr[i]
                index = i
        if self.arr[index] == -1:
            return '#'
        else:
            return chr(index)

    def Insert(self, char):
        # write code here
        index = ord(char)
        # 没有出现过
        if self.arr[index] == -1:
            self.arr[index] = self.index
            self.index += 1
        # 出现两次
        elif self.arr[index] >= 0:
            self.arr[index] = -2
        # 大于两次
        elif self.arr[index] == -2:
            pass


if __name__ == '__main__':
    s = Solution()
    ss = "google"
    ss = list(ss)
    for item in ss:
        s.Insert(item)
        res = s.FirstAppearingOnce()
        print(res)