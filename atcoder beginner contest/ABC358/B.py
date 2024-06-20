n,a = map(int,input().split())

t = list(map(int,input().split()))

can_time = 0
now_time = 0

for i in range(n):
    if can_time < t[i]:
        can_time = t[i]
    now_time = can_time
    can_time = now_time + a
    print(can_time)