k, n, w = map(int, raw_input().split(' '))

print max(w*(w+1)*k/2 - n, 0)
