def insertion_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i, 0, -1):
            if arr[j] < arr[j - 1]:
                temp = arr[j]
                arr[j] = arr[j - 1]
                arr[j - 1] = temp
            else:
                break


arr = [1, 9, 12, 0, 5, 8, 7, 2]
insertion_sort(arr)
print(arr)
