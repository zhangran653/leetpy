# Definition for a binary tree node.
"""
https://leetcode-cn.com/problems/unique-binary-search-trees-ii/
95. 不同的二叉搜索树 II
给定一个整数 n，生成所有由 1 ... n 为节点所组成的二叉搜索树。

示例:

输入: 3
输出:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
解释:
以上的输出对应以下 5 种不同结构的二叉搜索树：

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

ref: https://www.colabug.com/3563530.html
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if not n:
            return []
        return self._generate_trees(1, n)

    def _generate_trees(self, start, end):
        if start > end:
            return [None]
        ret = []

        for i in range(start, end + 1):
            sub_left = self._generate_trees(start, i - 1)
            sub_right = self._generate_trees(i + 1, end)

            for left in sub_left:
                for right in sub_right:
                    root = TreeNode(i)
                    root.left = left
                    root.right = right
                    ret.append(root)
        return ret


if __name__ == '__main__':
    ret = Solution().generateTrees(3)
    print(ret)
