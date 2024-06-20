n = int(input())

from collections import deque
import sys
#再帰
sys.setrecursionlimit(10**9)

path = [deque() for _ in range(n + 1)]

max_w = 0

for i in range(1,n):
    d = list(map(int,input().split()))
    for j in range(1,len(d) + 1):
        path[i].append([d[j - 1],i + j])#iからi + jに行くにはd[j - 1]の重みが発生
        path[i + j].append([d[j - 1],i])#[重み,行き先]

# def dfs(now,is_count,w,visited):#現在地・カウントする回か否か・得た重み
#     global max_w
#     visited.add(now[1])
#     if max_w < w:
#         max_w = w
#     for next in path[now[1]]:
#         if next[1] in visited:
#             continue
#         plus = next[0] if is_count else 0
#         dfs(next,not is_count,w + plus,visited.copy())



# dfs([0,1],True,0,set())
# dfs([0,1],False,0,set())

dp = [0 for _ in range(n + 1)]

for i in range(1,n + 1):
    dp[i] = dp[i - 1]#前回までの最大値を入れておく
    for j in range(1,i + 1):
        for k in range(1,i + 1):
            if j + k > i:
                continue
            dp[i] = max(dp[i], dp[j] + dp[k])

print(max_w)