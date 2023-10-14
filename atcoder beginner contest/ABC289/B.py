N,M = map(int,input().split())

a = list(map(int,input().split()))

now = 0

from collections import deque

re_list = deque()

ans = []

for i in range(N):
    try:
        a[now]
    except:
        ans.append(i + 1)
        for j in re_list:
            ans.append(j)
        re_list.clear()
        continue
    if a[now] == i + 1:#現在レ点がついていれば
        re_list.appendleft(i + 1)
        now += 1

    else:
        ans.append(i + 1)
        for j in re_list:
            ans.append(j)
        re_list.clear()

print(*ans)