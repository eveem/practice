def merge(l, r):
    result = []
    i = 0
    j = 0
    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            result.append(l[i])
            i += 1
        else:
            result.append(r[j])
            j += 1

    while i < len(l):
        result.append(l[i])
        i += 1

    while j < len(r):
        result.append(r[j])
        j += 1

    return result


def sort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    l = sort(arr[:mid])
    r = sort(arr[mid:])
    return merge(l, r)


arr = [1, 9, 12, 0, 5, 8, 7, 2, 8, 11]
arr = sort(arr)
print(arr)
