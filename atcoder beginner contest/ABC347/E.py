n,q = map(int,input().split())

x = list(map(int,input().split()))
a = [0 for _ in range(n + 1)]

items = dict()
log = dict()


from collections import deque

#その時刻に何個のアイテムが存在していたか
time = [0 for _ in range(q)]

for item in range(q):
    if x[item] not in items:
        #クエリ：時間で保存
        items[x[item]] = item
    else:
        if x[item] in log:
            log[x[item]].append([items[x[item]],item])
        else:
            log[x[item]] = deque([[items[x[item]],item]])
        del items[x[item]]
    time[item] = len(items)

#個数の累積和
time_sum = [0 for _ in range(q + 1)]

for i in range(1,q + 1):
    time_sum[i] = time_sum[i - 1] + time[i - 1]

for l in log:
    for i in log[l]:
        a[l] += time_sum[i[1]] - time_sum[i[0]]
for i in items:
    a[i] += time_sum[-1] - time_sum[items[i]]

print(*a[1:])
