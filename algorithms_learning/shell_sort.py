def shell_sort(arr):
    n = len(arr)
    h = 1
    while h < n / 3:
        h = 3 * h + 1

    while h >= 1:
        for i in range(h, n):
            temp = arr[i]
            j = i
            while j >= h and arr[j - h] > temp:
                arr[j] = arr[j - h]
                j -= h
            arr[j] = temp
        h = h // 3


arr = [1, 9, 12, 0, 5, 8, 7, 2]
shell_sort(arr)
print(arr)
