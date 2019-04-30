# ------- merge sort --------
def merge_sort(arr):
    _merge_sort(arr, 0, len(arr) - 1)


def _merge_sort(arr, l, r):
    if l >= r:
        return
    mid = l + (r - l) // 2
    _merge_sort(arr, l, mid)
    _merge_sort(arr, mid + 1, r)
    if arr[mid + 1] < arr[mid]:
        _merge(arr, l, mid, r)


def _merge(arr, l, mid, r):
    aux = arr[l:r + 1]
    i = l
    j = mid + 1
    for k in range(l, r + 1):
        if i > mid:
            arr[k] = aux[j - l]
            j += 1
        elif j > r:
            arr[k] = aux[i - l]
            i += 1
        elif aux[i - l] < aux[j - l]:
            arr[k] = aux[i - l]
            i += 1
        else:
            arr[k] = aux[j - l]
            j += 1


def merge_sort_bu(arr):
    sz = 1
    while sz < len(arr):
        lo = 0
        while lo + sz - 1 <= len(arr):
            _merge(arr, lo, lo + sz - 1, min(lo + sz * 2 - 1, len(arr) - 1))
            lo = lo + sz * 2
        sz *= 2


# -------- merge sort --------

# -------- select sort -------
def select_sort(arr):
    for i in range(0, len(arr)):
        index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[index]:
                index = j
        arr[i], arr[index] = arr[index], arr[i]


# -------- select sort -------

# ------- insert sort -------
def insert_sort(arr):
    for i in range(1, len(arr)):
        min_index = i
        temp = arr[i]
        for j in range(i, 0, -1):
            if temp < arr[j - 1]:
                arr[j] = arr[j - 1]
                min_index = j - 1
            else:
                break
        arr[min_index] = temp


# ------- insert sort -------

if __name__ == '__main__':
    a = [354, 23, 65, 43, 1, 456, 43, 32, 76, 43, 675, 43, 23]

    merge_sort_bu(a)
    print(a)
