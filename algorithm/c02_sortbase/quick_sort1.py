"""
快速排序 v1
每次选取的标定点为index=0
对于近乎有序的数组退化为O(n^2)

"""


def quick_sort(arr):
    _quick_sort(arr, 0, len(arr) - 1)


def _quick_sort(arr, l, r):
    if l >= r:
        return
    p = _partition(arr, l, r)
    _quick_sort(arr, l, p - 1)
    _quick_sort(arr, p + 1, r)


def _partition(arr, l, r):
    v = arr[l]
    j = l

    for i in range(l + 1, r + 1):
        if arr[i] < v:
            arr[j + 1], arr[i] = arr[i], arr[j + 1]
            j += 1
    arr[l], arr[j] = arr[j], arr[l]
    return j


if __name__ == '__main__':
    a = [28, 6, 3, 123, 5, 3, 23, 54, 1, 34]
    quick_sort(a)
    print(a)
