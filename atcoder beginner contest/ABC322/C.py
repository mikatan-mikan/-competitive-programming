n,m = map(int,input().split())

a = list(map(int,input().split()))

ite = 0

for i in range(n):
    if a[ite] < i + 1:
        ite += 1
    print(a[ite] - (i + 1))