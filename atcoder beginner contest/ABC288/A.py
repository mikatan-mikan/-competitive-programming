N = int(input())

num = [list(map(int,input().split())) for _ in range(N)]

for i in range(N):
    print(num[i][0] + num[i][1])