a = str(input())
c = a.lower()

v = list(c.split( ))

i = 0
b = list()

while i != len(v) - 1:
    b.append(v[i][0])
    
    if b.count(b[i]) > 1:
        print('НЕТ')
        break
    i += 1
else:
    print('ДА')