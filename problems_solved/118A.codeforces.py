st = raw_input().lower()
st = ''.join(c for c in st if c not in 'aeiouy')

st = ''.join('.' + c for c in st)

print st