"""
题目描述
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，
并保证奇数和奇数，偶数和偶数之间的相对位置不变
"""

# 不改变顺序，相邻交换或移动
# 要求前奇后偶，若碰到前偶后奇就前后调整
# 没遍历一遍，最后一个肯定是调整好的


def reOrderArray(array):
    # write code here
    length = len(array)
    for i in range(length):
        for j in range(length-i-1): # 下面是j+1，会超索引，要减一
            # 前偶后奇就前后调整
            if array[j] % 2 == 0 and array[j+1] % 2 == 1:
                array[j], array[j+1] = array[j+1], array[j]
    return array


print(reOrderArray([1, 2, 3, 4, 5, 6, 7]))
