"""
https://leetcode-cn.com/problems/first-unique-character-in-a-string/
387. 字符串中的第一个唯一字符
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

案例:

s = "leetcode"
返回 0.

s = "loveleetcode",
返回 2.


注意事项：您可以假定该字符串只包含小写字母。

"""


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        if not s:
            return -1
        for w in s:
            d[w] = d.get(w, 0) + 1
        for i in range(0, len(s)):
            if d.get(s[i], 0) == 1:
                return i
        return -1
