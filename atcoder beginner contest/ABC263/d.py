from collections import deque


N,L,R = map(int,input().split())

a_list = list(map(int,input().split()))

ans_tmp = deque()

for x in range(N + 1):#xが0~Nの時の全通り
    ans_tmp.append([L for _ in range(x)] + a_list[x :N ])
#ans_tmpの一番小さい物を今度はy視点で後ろから見ていけばよいので
min_ = 10000000000000
y_c = deque()
for i in range(len(ans_tmp)):
    a = ans_tmp[i]
    if min_ > sum(a):
        y_c.clear()
        min_ = sum(a)
        y_c.append(a)
    elif min_ == sum(a):
        y_c.append(a)

ans_tmp.clear()
for i in range(len(y_c)):#最小になる可能性があるもの
    for y in range(N + 1):
        ans_tmp.append((R * y) + sum(y_c[i][0:N - y]))

print(min(ans_tmp))