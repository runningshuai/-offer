"""
题目描述
输入一个字符串,按字典序打印出该字符串中字符的所有排列。
例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
"""
class Solution:
    def Permutation(self, ss):
        # write code here
        if not ss:
            return []
        result, s = [], list(ss) # 字符串不支持赋值操作
        def dfs(x):
            # 递归结束条件
            if x == len(s):
                return result.append(''.join(s))
            # 中间扩展
            dic = set()
            for i in range(x, len(s)):
                # 交换完，继续递归
                if s[i] not in dic:
                    s[x], s[i] = s[i], s[x]
                    dic.add(s[i])
                    dfs(x+1)
                    # 调整回原来位置。只有得到一组结果之后，才会走到这里
                    s[x], s[i] = s[i], s[x]
        dfs(0)
        return sorted(result)