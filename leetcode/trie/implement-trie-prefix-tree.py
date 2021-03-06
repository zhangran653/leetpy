"""
https://leetcode-cn.com/problems/implement-trie-prefix-tree/
208. 实现 Trie (前缀树)
实现一个 Trie (前缀树)，包含 insert, search, 和 startsWith 这三个操作。

示例:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // 返回 true
trie.search("app");     // 返回 false
trie.startsWith("app"); // 返回 true
trie.insert("app");
trie.search("app");     // 返回 true
说明:

你可以假设所有的输入都是由小写字母 a-z 构成的。
保证所有输入均为非空字符串。

"""


class Trie(object):
    class _Node:
        def __init__(self, is_word=False):
            self.is_word = is_word
            self.next = dict()

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._root = self._Node()

    def insert(self, word):
        """
        Inserts a word into the trie.
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
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        cur = self._root
        for w in word:
            if not cur.next.get(w):
                return False
            cur = cur.next.get(w)
        return cur.is_word

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        cur = self._root
        for w in prefix:
            if not cur.next.get(w):
                return False
            cur = cur.next.get(w)
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
