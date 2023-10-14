n,m = map(int,input().split())

l = list(map(int,input().split()))

sum_l = sum(l)

from collections import deque

#それぞれの行に入っているものを管理
lines = [deque() for _ in range(m)]
lines_sum = [0 for _ in range(m)]

#まずは普通にn / mを超えるまで入れていく
now_iter = 0
for i in range(n):
    lines[now_iter].append(l[i])
    lines_sum[now_iter] += l[i] + 1
    if lines_sum[now_iter] > (sum_l / m) and now_iter != m - 1:
        lines_sum[now_iter] -= 1
        now_iter += 1

print(lines,sum_l)