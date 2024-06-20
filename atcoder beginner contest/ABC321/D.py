l = []

for j in range(1000):
    flg = True
    bef = 10
    n = str(j)
    for i in range(len(n)):
        if int(n[i]) < bef:
            bef = int(n[i])
        else:
            flg = False
            break
    if flg:
        l.append(j)

print(l[60])