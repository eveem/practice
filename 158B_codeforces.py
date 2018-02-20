n = int(raw_input())
st = raw_input().split(' ')
st = sorted([int(i) for i in st])
co = [0]

for i in range(1, 5):
    co.append(st.count(i))

# print co[1:]

r = co[4]
co[4] = 0

if co[3] > co[1]:
    # if remain 3 we should added 3 then end if and goto calculate 1 and 2
    r += co[1]
    co[3] -= co[1]
    co[1] = 0
    r += co[3]
else:
    # remain 1 and 2 don't need to add 1 because we use 1 in next step
    r += co[3]
    co[1] -= co[3]

co[3] = 0

# 2 + 2 calculate
if co[2] % 2 == 0:
    r += co[2] / 2
    co[2] = 0
else:
    r += int(co[2] / 2)
    co[2] = 1

if co[1] % 4 == 0:
    r += co[1] /4
    co[1] = 0
else:
    r += int(co[1] / 4)
    co[1] %= 4

if co[2] == 1:
    r += 1
    co[2] = 0
    co[1] -= 2

if co[1] > 0:
    r += 1

# print co[1:]

print r