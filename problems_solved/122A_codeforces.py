def check(n):
    for i in range(1, 1001):
        if i % 4 == 0 or i % 7 == 0 or check_47(str(i)):
            if n % i == 0:
                return "YES"
    return "NO"

def check_47(c):
    if c.replace('4', '').replace('7', '') == '':
        return True
    return False

s = raw_input()

if check_47(s):
    print "YES"
else:
    print check(int(s))