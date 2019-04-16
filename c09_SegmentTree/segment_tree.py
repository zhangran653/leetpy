class SegmentTree:
    def __init__(self, arr, merger):
        """线段树相当于将数组用一棵树重新表示"""
        if not isinstance(arr, list) or not arr or not merger:
            raise ValueError('Can not initialize empty array.')
        self._data = arr[:]
        self._tree = [None] * 4 * len(arr)
        self._merger = merger
        if arr:
            self._build_segment_tree(tree_index=0, l=0, r=len(self._data) - 1)

    def get_size(self):
        return len(self._data)

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    # 在tree_index位置创建表示区间[l...r]的线段树
    # 左右的端点l, r
    def _build_segment_tree(self, tree_index, l, r):
        if l == r:
            self._tree[tree_index] = self._data[l]
            return
        left_tree_index = self._left_child(tree_index)
        right_tree_index = self._right_child(tree_index)
        mid = l + (r - l) // 2
        self._build_segment_tree(left_tree_index, l, mid)
        self._build_segment_tree(right_tree_index, mid + 1, r)
        self._tree[tree_index] = self._merger(
            self._tree[left_tree_index],
            self._tree[right_tree_index]
        )

    def query(self, query_l, query_r):
        if query_l < 0 or query_l >= len(self._data) or \
                query_r < 0 or query_r >= len(self._data) or \
                query_l > query_r:
            raise ValueError('Index is illegal.')

        return self._query(0, 0, len(self._data) - 1, query_l, query_r)

    def _query(self, tree_index, l, r, query_l, query_r):
        if l == query_l and r == query_r:
            return self._tree[tree_index]

        left_tree_index = self._left_child(tree_index)
        right_tree_index = self._right_child(tree_index)
        mid = l + (r - l) // 2
        if query_l >= mid + 1:
            return self._query(right_tree_index, mid + 1, r, query_l, query_r)
        elif query_r <= mid:
            return self._query(left_tree_index, l, mid, query_l, mid)
        else:
            left_tree_result = self._query(left_tree_index, l, mid, query_l, mid)
            right_tree_result = self._query(right_tree_index, mid + 1, r, mid + 1, query_r)
            return self._merger(left_tree_result, right_tree_result)
