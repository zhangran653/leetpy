"""
快速排序 v3
随机选取标定点

选择i，j
arr[l,i] <= arr[l]
arr[j,r] >= arr[l]

这样对于值=arr[l] 将平均分在两边

"""
import random
from time import time


def quick_sort(arr):
    random.seed(time())
    _quick_sort(arr, 0, len(arr) - 1)


def _quick_sort(arr, l, r):
    if l >= r:
        return
    p = _partition(arr, l, r)
    _quick_sort(arr, l, p - 1)
    _quick_sort(arr, p + 1, r)


def _partition(arr, l, r):
    index = random.randint(l, r)
    arr[l], arr[index] = arr[index], arr[l]
    v = arr[l]
    i = l + 1
    j = r
    while True:
        while i <= r and arr[i] < v:
            i += 1

        while j >= l + 1 and arr[j] > v:
            j -= 1
        if i > j:
            break
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1

    arr[l], arr[j] = arr[j], arr[l]
    return j


if __name__ == '__main__':
    a = [28, 6, 3, 123, 5, 3, 23, 54, 1, 34]
    quick_sort(a)
    print(a)
