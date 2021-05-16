n = int(input())

x = input()
x = x.split(' ')[1:]

y = input()
y = y.split(' ')[1:]

x = x + y

print("I become the guy." if len(set(x)) == n else "Oh, my keyboard!")