"""
题目描述
从上往下打印出二叉树的每个节点，同层节点从左至右打印
"""


def PrintFromTopToBottom(root):
    # write code here
    # 层次遍历
    # 存节点，存结果
    queue, res = [], []
    if not root:
        return res
    queue.append(root)
    while queue:
        node = queue.pop(0)
        res.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return res