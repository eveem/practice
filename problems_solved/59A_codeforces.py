text = input()

up = 0
lw = 0

for char in text:
	if char.isupper():
		up += 1
	else:
		lw += 1

if up > lw:
	print(text.upper())
else:
	print(text.lower())
