"""
题目描述
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
思路：
把数字转化成字符串
实现排序，要改变排序规则，通过两个字符串拼接后的大小来决定原来字符串的大小
"""
# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        if not numbers:
            return ''
        numbers = [str(item) for item in numbers]
        result = self.quick_sort(numbers)
        return ''.join(result)

    def quick_sort(self, arr):
        # 停止条件
        if len(arr) < 2:
            return arr
        else:
            less, great = [], []
            pivot = arr[0]
            for item in arr[1:]:
                if item + pivot > pivot + item:
                    great.append(item)
                else:
                    less.append(item)
            return self.quick_sort(less) + [pivot] + self.quick_sort(great)

if __name__ == '__main__':
    s = Solution()
    res = s.PrintMinNumber([3, 32, 321])
    print(res)