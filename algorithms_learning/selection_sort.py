def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        m_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[m_idx]:
                m_idx = j
        temp = arr[i]
        arr[i] = arr[m_idx]
        arr[m_idx] = temp


arr = [1, 9, 12, 0, 5, 8, 7, 2]
selection_sort(arr)
print(arr)
