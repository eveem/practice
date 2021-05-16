n = int(input())
x = input()
print(sum(int(i) for i in x.split(' '))/(100 * n) * 100)