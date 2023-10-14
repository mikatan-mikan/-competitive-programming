n = int(input())

a = list(map(int,input().split()))

from collections import deque
import sys

sys.setrecursionlimit(10**9)

visited = set()
visited_d = deque()

def p():
    ans = deque()
    end = visited_d[-1]#最後と一致するところまでが閉路
    for i in range(len(visited_d)):
        if visited_d[-(i + 1)] == end and i != 0:
            print(len(ans))
            print(*ans)
            exit()
        ans.appendleft(visited_d[-(i + 1)])

def dfs(now):
    visited.add(now)
    visited_d.append(now)
    if a[now - 1] not in visited: #まだ行ったことが無い場所なら
        dfs(a[now - 1])# そこに進む
    else:# 行ったことがあるならそこで閉路が出来ていることが分かるので
        visited_d.append(a[now - 1])#最後の場所を追加して
        p()#出力


dfs(1)