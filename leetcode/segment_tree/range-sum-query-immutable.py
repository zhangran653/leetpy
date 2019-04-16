"""
https://leetcode-cn.com/problems/range-sum-query-immutable/
303. 区域和检索 - 数组不可变
给定一个整数数组  nums，求出数组从索引 i 到 j  (i ≤ j) 范围内元素的总和，包含 i,  j 两点。

示例：

给定 nums = [-2, 0, 3, -5, 2, -1]，求和函数为 sumRange()

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
说明:

你可以假设数组不可变。
会多次调用 sumRange 方法。
"""


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self._data = nums[:]
        self._tree = [None] * 4 * len(nums)
        self._merger = lambda a, b: a + b
        if nums:
            self._build_segment_tree(0, 0, len(self._data) - 1)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return 0 if not self._data else self._query(0, 0, len(self._data) - 1, i, j)

    def _build_segment_tree(self, tree_index, l, r):
        if l == r:
            self._tree[tree_index] = self._data[l]
            return
        left_index = self._left_index(tree_index)
        right_index = self._right_index(tree_index)
        mid = l + (r - l) // 2
        self._build_segment_tree(left_index, l, mid)
        self._build_segment_tree(right_index, mid + 1, r)
        self._tree[tree_index] = self._merger(self._tree[left_index], self._tree[right_index])

    def _left_index(self, index):
        return index * 2 + 1

    def _right_index(self, index):
        return index * 2 + 2

    def _query(self, tree_index, l, r, query_l, query_r):
        if l == query_l and r == query_r:
            return self._tree[tree_index]

        left_index = self._left_index(tree_index)
        right_index = self._right_index(tree_index)
        mid = l + (r - l) // 2
        if query_l >= mid + 1:
            return self._query(right_index, mid + 1, r, query_l, query_r)
        elif query_r <= mid:
            return self._query(left_index, l, mid, query_l, query_r)
        else:
            left_result = self._query(left_index, l, mid, query_l, mid)
            right_result = self._query(right_index, mid + 1, r, mid + 1, query_r)
            return self._merger(left_result, right_result)


if __name__ == '__main__':
    print(NumArray([]).sumRange(0, 2))
