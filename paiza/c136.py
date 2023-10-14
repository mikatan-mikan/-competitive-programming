n = int(input())

x = [int(input()) for _ in range(n)]

now = x[0]

down = 0
up = 0
down_max = 0
up_max = 0

for i in range(1,n):
    if x[i] > now:
        down = 0
        up += 1
        up_max = max(up_max,up)
    elif x[i] < now:
        up = 0
        down += 1
        down_max = max(down_max,down)
    now = x[i]

print(down_max,up_max)