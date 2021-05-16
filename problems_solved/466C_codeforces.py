n = int(input())
arr = [int(i) for i in input().split()]

S = sum(arr)

if S % 3 != 0:
    print(0)
else:
    s = S // 3
    ss = 0
    cnt = [0 for _ in range(n)]

    for i in range(n - 1, -1, -1):
        ss += arr[i]
        if ss == s:
            cnt[i] = 1

    for i in range(n - 2, -1, -1):
        cnt[i] += cnt[i + 1]
    
    ans = 0
    ss = 00
    for i in range(0, n - 2):
        ss += arr[i]
        
        if ss == s:
            ans += cnt[i + 2]
    print(ans)
    