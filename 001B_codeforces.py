import re

n = int(raw_input())
s = ''

for i in range(0, n):
    s = raw_input()
    t = re.match('R(\d+)C(\d+)', s)

    if t:
        nc = int(t.group(2))
        nr = t.group(1)
        while nc > 0:
            nr = chr(65 + (nc - 1) % 26) + nr
            nc -= 1
            nc /= 26
        print nr
    else:
        t = re.match('(\D+)(\d+)', s)
        r = 'R' + t.group(2) + 'C'
        nc = 0
        for j in t.group(1):
            nc = nc * 26 + ord(j) - ord('A') + 1
        r += str(nc)
        print r