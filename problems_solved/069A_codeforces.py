n = int(raw_input())
a = b = c = 0

for i in range(0, n):
    s = map(int, raw_input().split())
    a += s[0]
    b += s[1]
    c += s[2]

print "YES" if a == b == c == 0 else "NO"

