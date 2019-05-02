def printWelcome():
    print('WELCOME', end='')

def printHifen(t):
    for i in range(t):
        print('-', end='')

def printTriangle(t):
    x = '.|.'
    print(x * t, end='')

x = input()
x = x.split(' ')
n = int(x[0])
m = int(x[1])

mid = n // 2 + 1
d = 1
ic = 1

for i in range(1, n + 1):
    if i == mid:
        printHifen((m - 7)//2)
        printWelcome()
        printHifen((m - 7)//2)
        ic = -1
        d -= 2
    else:
        printHifen((m - 3 * d)//2)
        printTriangle(d)
        printHifen((m - 3 * d)//2)
        d += 2 * ic

    print()
