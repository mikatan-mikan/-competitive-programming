n = int(input())

a = [list(map(int,input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if a[i][j] == 1:
            print(j + 1,end = " ")
    print()