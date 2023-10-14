n,m = map(int,input().split())

p = [list(map(int,input().split())) for _ in range(n)]

cnt = 0

for i in range(n):
    for j in range(n):
        if p[j][i] >= m:
            break
        if j == n - 1:
            if cnt != 0:
                print(" ", end = "")
            print(i + 1, end = "")
            cnt += 1

if cnt == 0:
    print("wait")
