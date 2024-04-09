s = 7 ** 3096 + 9 ** 1024 - 12
t = ''
while s != 0:
    t += str(s % 9)
    s //= 9

print(t.count('3'))