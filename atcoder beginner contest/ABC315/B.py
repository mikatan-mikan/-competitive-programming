m = int(input())

d = list(map(int,input().split()))

sd = sum(d)
mid = sd//2

for i in range(m):
    for j in range(d[i]):
        sd -= 1
        if sd == mid:
            print(i+1,j + 1)
            break