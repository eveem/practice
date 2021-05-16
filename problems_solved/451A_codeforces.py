x = input()
x = x.split()
a = int(x[0])
b = int(x[1])

if a < b:
	c = a
else:
	c = b

print('Akshat' if c % 2 else 'Malvika')


