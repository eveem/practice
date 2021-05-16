n = int(raw_input())
s = raw_input().split(' ')

s = [int(i) for i in s]
s.sort()

m = c = 0

while m <= sum(s):
    m += s.pop()
    c += 1

print c