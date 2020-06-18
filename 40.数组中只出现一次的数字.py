"""
题目描述
一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。
思路
在34题里，通过列表来建立hash,列表的索引值当作key，列表的值存value
这里是不是也可以这样呢？首先key有很多，要是数组元素特别大，又或者出现不连续的情况，此时列表长度很大，占很多空间。
还有只有两个数不同，其他都是成对出现的，这是重要的信息。用位异或运算
首先：位运算中异或的性质：两个相同数字异或=0，一个数和0异或还是它本身。
1、消灭成对出现的数
当只有一个数出现一次时，我们把数组中所有的数，依次异或运算，最后剩下的就是落单的数，因为成对儿出现的都抵消了。
2、拆分不同的两个数
依照这个思路，我们来看两个数（我们假设是AB）出现一次的数组。我们首先还是先异或，剩下的数字肯定是A、B异或的结果，
这个结果的二进制中的1，表现的是A和B的不同的位。
我们就取第一个1所在的位数，假设是第3位，接着把原数组分成两组，分组标准是第3位是否为1。如此，相同的数肯定在一个组，
因为相同数字所有位都相同，而不同的数，肯定不在一组。然后把这两个组按照最开始的思路，依次异或，
剩余的两个结果就是这两个只出现一次的数字。
"""
# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        if len(array) == 2:
            return array
        # 全部数字异或
        bit_result = self.yihuo(array)
        # 拆分结果，先按位不同拆成两个数组，然后每个数组内部异或，最后异或结果就是要找的数
        # 查找异或结果位为1的索引
        flag = 1
        while True:
            if bit_result & flag:
                break
            flag = flag << 1
        # 分开原数组为两部分
        arr1, arr2 = [], []
        for item in array:
            if item & flag:
                arr1.append(item)
            else:
                arr2.append(item)
        # 分开的数组各自异或
        num1 = self.yihuo(arr1)
        num2 = self.yihuo(arr2)
        return [num1, num2]
    def yihuo(self, arr):
        result = 0
        for item in arr:
            result = result ^ item
        return result


if __name__ == '__main__':
    s = Solution()
    result = s.FindNumsAppearOnce([1, 2, 4, 5, 1, 5, 2, 6])
    print(result)