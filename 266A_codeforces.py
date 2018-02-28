n = int(raw_input())
s = raw_input()

print sum(i == j for i, j in zip(s, s[1:]))