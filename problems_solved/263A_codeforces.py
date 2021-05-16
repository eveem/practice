for i in range(0, 5):
    m = raw_input().split(' ')
    if '1' in m:
        print abs(2 - i) + abs(2 - m.index('1'))