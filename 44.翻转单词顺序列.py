"""
题目描述
牛客最近来了一个新员工Fish，每天早晨总是会拿着一本英文杂志，写些句子在本子上。
同事Cat对Fish写的内容颇感兴趣，有一天他向Fish借来翻看，但却读不懂它的意思。
例如，“student. a am I”。后来才意识到，这家伙原来把句子单词的顺序翻转了，正确的句子应该是“I am a student.”。
Cat对一一的翻转这些单词顺序可不在行，你能帮助他么?
思路：
你能帮助他吗？说实话我不想帮他，为了找工作不得不帮他。。。
单词按空格切分，然后单个单词反转
split的坑，对于" ",若按split(" "),可切出两个空字符串组成的列表，split()切出的列表为空
"""
class Solution2:
    def ReverseSentence(self, s):
        # write code here
        # 不用内置函数split(),反转还是按单个字母操作
        # 翻转整个字符串，然后按空格切出字符串，再进行翻转
        res = []
        s = self.reverse(s)
        left = -1
        for i in range(len(s)):
            if s[i] == ' ':
                right = i
                res.append(self.reverse(s[left+1:right])) # 切片是注意左边界
                left = right
            # 最后一个字符没有空格的处理
            if i == len(s) - 1:
                res.append(self.reverse(s[left + 1:]))
        return " ".join(res)

    def reverse(self, ss):
        if len(ss) <= 1:
            return ss
        # 用双指针，前后交换
        ss = list(ss)
        i, j = 0, len(ss) - 1
        while i < j:
            ss[i], ss[j] = ss[j], ss[i]
            i += 1
            j -= 1
        return ''.join(ss)


class Solution1:
    def ReverseSentence(self, s):
        # write code here
        res = []
        # split
        s = self.reverse(s)
        for item in s.split(' '):
            res.append(self.reverse(item))
        return ' '.join(res)

    def reverse(self, ss):
        if len(ss) <= 1:
            return ss
        return ss[::-1]



if __name__ == '__main__':
    s = Solution2()
    print(s.ReverseSentence('I am a student.'))