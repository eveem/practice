def exch(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def partition(arr, lo, hi):
    i = lo + 1
    j = hi

    while True:
        while arr[i] < arr[lo] and i != hi:
            i += 1

        while arr[lo] < arr[j] and j != lo:
            j -= 1

        if i >= j:
            break

        exch(arr, i, j)

    exch(arr, lo, j)
    return j


def sort(arr, lo, hi):
    if hi <= lo:
        return

    j = partition(arr, lo, hi)
    sort(arr, lo, j - 1)
    sort(arr, j + 1, hi)


arr = [1, 9, 12, 0, 5, 8, 7, 2, 8, 11]
sort(arr, 0, len(arr) - 1)
print(arr)
