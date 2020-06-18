"""
题目描述
把只包含质因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含质因子7。
习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
思路：
从1开始，我们只用比较3个数：u2:用于乘2的数，u3:乘3的数，u5:乘5的数，然后取最小的数
最小的数取完之后，更新当前的数，例如u2 * 2
一直循环，直到取N个
"""
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index < 7:
            return index
        ugly = [1]
        # 初始化待比较的三个数,这三个数都是乘的同一个数，只有这个数消费掉，才可以乘下一个
        # 2， 3， 5需要乘的序列就是丑数序列，即第一次都乘1，第二次都乘2， 第三次都乘3
        # 需要注意的是，不是同时乘的，是当前这个数被消费掉才去乘的
        u2, u3, u5 = 2, 3, 5
        # 记录乘了第几个
        i2, i3, i5 = 0, 0, 0
        while len(ugly) < index:
            temp = min(u2, u3, u5)
            ugly.append(temp)
            # 需要找到哪一个最小的数被取走了，然后开始乘下一个数，并更新
            if temp == u2:
                i2 += 1
                u2 = 2 * ugly[i2]
            if temp == u3:
                i3 += 1
                u3 = 3 * ugly[i3]
            if temp == u5:
                i5 += 1
                u5 = 5 * ugly[i5]
        return ugly[-1]


if __name__ == '__main__':
    s = Solution()
    print(s.GetUglyNumber_Solution(11))
