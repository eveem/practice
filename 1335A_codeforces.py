n = int(input())

for i in range(n):
    a = int(input())
    print(int(a / 2) if a % 2 != 0 else int(a / 2) - 1)