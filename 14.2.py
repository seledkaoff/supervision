xAlf = '0123456789AB'
yAlf = '0123456789ABCD'
for x in xAlf:
    for y in yAlf:
        temp = int(x + '57AB', 12) + int(y + 'CD' + x + x, 14)
        if temp % 96 == 0:
            print(temp, str(temp // 48) * 2)