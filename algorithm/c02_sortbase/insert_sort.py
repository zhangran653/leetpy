"""
插入排序
https://visualgo.net/zh/sorting
"""


def insert_sort(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
            else:
                break


if __name__ == "__main__":
    a = [24, 23, 5, 2, 6, 8, 3, 1, 8]
    insert_sort(a)
    print(a)
