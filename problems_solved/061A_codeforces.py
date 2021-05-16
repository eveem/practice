a = input()
b = input()
ans = ''

for i, j in zip(a, b):
	if int(i) + int(j) == 2:
		ans += '0'
	else:
		ans += str(int(i) + int(j))

print(ans)