n = int(input())
a = sorted(list(map(int,input().split())))

bef = a[0] - 1

for i in range(n):
    if a[i] == bef + 1:
        bef = a[i]
        continue
    else:
        print(a[i] - 1)
        exit()