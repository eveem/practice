s = raw_input()
print [s, s.swapcase()][s[1:].upper() == s[1:]]
