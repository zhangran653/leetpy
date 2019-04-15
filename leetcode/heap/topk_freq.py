"""
https://leetcode-cn.com/problems/top-k-frequent-words/
692. 前K个高频单词

给一非空的单词列表，返回前 k 个出现次数最多的单词。

返回的答案应该按单词出现频率由高到低排序。如果不同的单词有相同出现频率，按字母顺序排序。

示例 1：

输入: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
输出: ["i", "love"]
解析: "i" 和 "love" 为出现次数最多的两个单词，均为2次。
    注意，按字母顺序 "i" 在 "love" 之前。


示例 2：

输入: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
输出: ["the", "is", "sunny", "day"]
解析: "the", "is", "sunny" 和 "day" 是出现次数最多的四个单词，
    出现次数依次为 4, 3, 2 和 1 次。


注意：

假定 k 总为有效值， 1 ≤ k ≤ 集合元素数。
输入的单词均由小写字母组成。


扩展练习：

尝试以 O(n log k) 时间复杂度和 O(n) 空间复杂度解决。

ref: https://www.jianshu.com/p/5c55282b1d54
"""


class Solution(object):
    def topKFrequent(self, words, k):
        import heapq as hq
        class Freq:
            def __init__(self, word, freq):
                self.word = word
                self.freq = freq

            def __lt__(self, other):
                if self.freq < other.freq:
                    return -1
                if self.freq == other.freq and self.word > other.word:
                    return -1

        d = {}
        for w in words:
            d[w] = d.get(w, 0) + 1
        data = []
        for key, val in d.items():
            f = Freq(key, val)
            if len(data) < k:
                hq.heappush(data, f)
            elif data[0] < f:
                hq.heapreplace(data, f)

        return [x.word for x in hq.nsmallest(k, data)][::-1]

    def topKFrequent1(self, words, k):
        import heapq
        import collections
        return [x[1] for x in heapq.nsmallest(k, [(v, k) for k, v in collections.Counter(words).items()],
                                              key=lambda a: (-a[0], a[1]))]


if __name__ == '__main__':
    print(Solution().topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2))
