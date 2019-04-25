"""
选择排序

"""


def sort(arr):
    for i in range(0, len(arr)):
        min_index = i
        for j in range(i, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


if __name__ == '__main__':
    arr = [1, 3, 5, 1, 7, 4, 7, 33, 8, 9, 4, 2]
    sort(arr)
    print(arr)
