from string import ascii_uppercase, digits
tempLetter = ascii_uppercase.index("G")
alf = digits + ascii_uppercase[:tempLetter + 1]

for x in range(len(alf), 36):
    for y in alf:
        temp = int(y + 'DGE12', x) - int('9' + y + 'CFF4', x)
        if '555' in str(temp):
            print(x)
    tempLetter += 1
    alf += ascii_uppercase[tempLetter]
