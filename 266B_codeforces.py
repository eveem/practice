n = map(int, raw_input().split())
s = raw_input()

while n[1] > 0:
    s = s.replace('BG', 'GB')
    n[1] -= 1

print s