import string

c = []
s = raw_input().lower()
for i in s:
    if i not in c:
        c.append(i)

print "CHAT WITH HER!" if len(c) % 2 == 0 else "IGNORE HIM!"