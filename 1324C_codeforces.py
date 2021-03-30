n = int(input())
for i in range(n):
    s = input()
    count = 1
    m = 0
    for j in s:
        if j == 'R':
            if count > m:
                m = count
            count = 0
        count += 1
    if count > m:
        m = count
    print(m)