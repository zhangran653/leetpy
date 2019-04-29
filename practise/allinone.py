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


# -------- merge sort --------


if __name__ == '__main__':
    a = [354, 23, 65, 43, 1, 456, 43, 32, 76, 43, 675, 43, 23]

    merge_sort(a)
    print(a)
