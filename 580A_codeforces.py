n = int(input())
arr = [int(i) for i in input().split()]
m = 1
count = 1

for i in range(1, n):
    if arr[i - 1] <= arr[i]:
        count += 1
    else:
        count = 1
    
    if count > m:
        m = count

print(m)