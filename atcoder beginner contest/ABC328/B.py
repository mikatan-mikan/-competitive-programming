n = int(input())

d = list(map(int,input().split()))

cnt = 0

for month in range(1,n + 1):
    for day in range(1,d[month - 1] + 1):
        isbreak = False
        dat = str(month) + str(day)
        #全ての文字が同じならcnt++
        ck = dat[0]
        for i in dat:
            if i != ck:
                isbreak = True
                break
        if not isbreak:
            cnt += 1


print(cnt)