n = int(raw_input())
r = 0

for i in range(0, n):
    st = raw_input()
    if '-' in st:
        r -= 1
    elif '+' in st:
        r += 1
    
print r