n = int(input())

for i in range(n):
    a, b = [int(k) for k in input().split(' ')]
    print((a // b + 1) * b - a if a % b != 0 else 0)