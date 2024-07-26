n,t,p = map(int,input().split())

l = list(map(int,input().split()))

p_cnt = 0

for i in l:
    if i >= t:
        p_cnt += 1

if p_cnt >= p:
    print(0)
    exit()

day = 0

while True:
    day += 1
    for i in range(len(l)):
        l[i] += 1
        if l[i] == t:
            p_cnt += 1
    if p_cnt >= p:
        print(day)
        exit()