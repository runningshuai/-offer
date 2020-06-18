"""
题目描述
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则输出Yes,否则输出No。
假设输入的数组的任意两个数字都互不相同。
二叉搜索树：
1、若左子树不为空，则左子树的所有结点的值均小于它的根节点的值
1、若右子树不为空，则右子树所有节点的值均大于它的根节点的值
后续遍历结果
"""


def VerifySquenceOfBST(sequence):
    # 牛客离案例，空为非二叉搜索树
    if not sequence:
        return False
    root = sequence[-1]
    length = len(sequence)
    i = 0
    # 左子树比根节点小，顺便找到分割点
    for i in range(length):
        if sequence[i] > root:
            break
    # 右子节点比root大
    for j in range(i, length):
        if sequence[j] < root:
            return False
    # sequence.pop(),只有一个元素时，没有左子树，i=0, 没有移动，j还是从0开始，造成错误判断
    # sequence 不加pop，i,可以相后移动
    # 有分开节点时
    left, right = True, True
    # 有左子树，同时避免为空时返回False
    if i > 0 and sequence[:i]:
        left = VerifySquenceOfBST(sequence[:i])
        # 有右子树
    if i < length and sequence[i:-1]:
        right = VerifySquenceOfBST(sequence[i:-1])
    return left and right

print(VerifySquenceOfBST([4,6,7,5]))