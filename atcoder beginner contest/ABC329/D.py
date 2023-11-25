n,m = map(int,input().split())

a = list(map(int,input().split()))

from sortedcontainers import SortedList

#現在の得票数を管理(得票数,i番目の人)
v = [0 for _ in range(n + 1)]

#現在の最大得票数
max_v = 0
now_win = 1000000000

for i in range(len(a)):
    v[a[i]] += 1
    if v[a[i]] > max_v:
        max_v = v[a[i]]
        now_win = a[i]
    elif v[a[i]] == max_v:
        if a[i] < now_win:
            now_win = a[i]
    print(now_win)
