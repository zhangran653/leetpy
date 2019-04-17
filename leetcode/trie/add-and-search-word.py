"""
https://leetcode-cn.com/problems/add-and-search-word-data-structure-design/
211. 添加与搜索单词 - 数据结构设计
设计一个支持以下两种操作的数据结构：

void addWord(word)
bool search(word)
search(word) 可以搜索文字或正则表达式字符串，字符串只包含字母 . 或 a-z 。 . 可以表示任何一个字母。

示例:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
说明:

你可以假设所有单词都是由小写字母 a-z 组成的。
"""


class WordDictionary(object):
    class _Node:
        def __init__(self, is_word=False):
            self.is_word = is_word
            self.next = dict()

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._root = self._Node()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        cur = self._root
        for w in word:
            if not cur.next.get(w):
                cur.next[w] = self._Node()
            cur = cur.next.get(w)
        if not cur.is_word:
            cur.is_word = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self._search(self._root, word, 0)

    def _search(self, node, word, index):
        if index == len(word):
            return node.is_word

        c = word[index]
        if c != '.':
            if not node.next.get(c):
                return False
            return self._search(node.next.get(c), word, index + 1)
        else:
            for k in node.next.keys():
                if self._search(node.next.get(k), word, index + 1):
                    return True
            return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
