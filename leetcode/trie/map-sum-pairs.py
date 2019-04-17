"""
https://leetcode-cn.com/problems/map-sum-pairs/
677. 键值映射
实现一个 MapSum 类里的两个方法，insert 和 sum。

对于方法 insert，你将得到一对（字符串，整数）的键值对。字符串表示键，整数表示值。如果键已经存在，那么原来的键值对将被替代成新的键值对。

对于方法 sum，你将得到一个表示前缀的字符串，你需要返回所有以该前缀开头的键的值的总和。

示例 1:

输入: insert("apple", 3), 输出: Null
输入: sum("ap"), 输出: 3
输入: insert("app", 2), 输出: Null
输入: sum("ap"), 输出: 5
"""


class MapSum(object):
    class _Node:
        def __init__(self, value=0):
            self.value = value
            self.next = dict()

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._root = self._Node()

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: None
        """
        cur = self._root
        for w in key:
            if not cur.next.get(w):
                cur.next[w] = self._Node()
            cur = cur.next.get(w)
        cur.value = val

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        cur = self._root
        for p in prefix:
            if not cur.next.get(p):
                return 0
            cur = cur.next.get(p)
        return self._sum(cur)

    def _sum(self, node):
        res = node.value
        for k in node.next.keys():
            res += self._sum(node.next.get(k))
        return res
# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
