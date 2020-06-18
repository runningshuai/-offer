"""
题目描述
在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置,
如果没有则返回 -1（需要区分大小写）.（从0开始计数）
思路
哈希的思想，不直接建立哈希；因为是字母，字母的数量有限，大小写26*2 = 52；可以用列表代替，列表的索引代替哈希值，
列表的值存这个字母出现了多少次。字母转化成数字，但大写的数字后有6个其它字符，然后才是小写字符。
最后的列表长度52 + 6 = 58, 中间的6个用不到。
这样列表中值为1的，就是出现了1次。由于是按字母排序，不确定哪个1是第一次出现的，所以还要再遍历一次。
ps: 65 - 90:大写字母，97 - 122：小写字母，中间6个是[ ,\, ]，^， ` ；减去65，从0开始
需要注意的，int 不能把字母转化成数字，用ord，传入单字符，返回数字
"""
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        index_hash = [0] * 58
        for i in s:
            index_hash[ord(i) - 65] += 1
        index = 0
        for j in s:
            if index_hash[ord(j) - 65] == 1:
                return index
            index += 1
        # 没有合适的
        return -1

if __name__ == '__main__':
    s = Solution()
    print(s.FirstNotRepeatingChar('google'))