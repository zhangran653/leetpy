# Definition for a binary tree node.
"""
https://leetcode-cn.com/problems/binary-tree-inorder-traversal/
94. 二叉树的中序遍历
给定一个二叉树，返回它的中序 遍历。

示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,3,2]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？

ref: https://blog.csdn.net/zgaoq/article/details/79089819,https://segmentfault.com/a/1190000011629742
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        ret = []
        self._inorderTraversal(root, ret)
        return ret

    def _inorderTraversal(self, node, ret=None):
        if not node:
            return ret
        self._inorderTraversal(node.left, ret)
        ret.append(node.val)
        self._inorderTraversal(node.right, ret)

    def inorderTraversal_NR(self, root):
        """
        非递归
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        ret = []
        stack.append(root)
        cur = root
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            if stack:
                cur = stack.pop()
                ret.append(cur.val)
                cur = cur.right
        return ret
