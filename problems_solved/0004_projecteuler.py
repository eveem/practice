def isPalindrome (st):
    if st[0] == st[5] and st[1] == st[4] and st[2] == st[3]:
        return True
    return False

ans = False
for i in range(999, 99, -1):
    for j in range(999, 99, -1):
        result = i * j
        if len(str(result)) == 6 and isPalindrome(str(result)):
            ans = True
            print result