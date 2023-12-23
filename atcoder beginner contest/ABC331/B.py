import sys
sys.setrecursionlimit(10**9)

n,s,m,l = map(int,input().split())

ans = 10**9

def dfs(now,cost):
    global ans
    if cost > ans:
        return
    if now <= 0:
        ans = min(ans,cost)
        return
    dfs(now - 12,cost + l)
    dfs(now - 8,cost + m)
    dfs(now - 6,cost + s)

dfs(n,0)
print(ans)