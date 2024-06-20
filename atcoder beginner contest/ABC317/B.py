n = int(input())

area = [[False for _ in range(101)] for _ in range(101)]

for i in range(n):
    a,b,c,d = map(int,input().split())
    for j in range(c,d):
        for k in range(a,b):
            area[k][j] = True


cnt = 0

for i in area:
    for j in i:
        if j == True:
            cnt += 1


print(cnt)