n,m,p = map(int,input().split())

cnt = 0

if p == m: m = 0

for i in range(1,n + 1):
    if i % p == m:
        cnt += 1
print(cnt)