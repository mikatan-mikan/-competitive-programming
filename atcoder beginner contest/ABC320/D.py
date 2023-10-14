import sys
sys.setrecursionlimit(10**9)

n,m = map(int,input().split())

path = [set() for _ in range(n + 1)]
ans = ["undecidable" for _ in range(n + 1)]

for i in range(m):
    a,b,x,y = map(int,input().split())
    path[a].add((b,x,y))
    path[b].add((a,-x,-y))#bから見てaは逆の位置

visited = set()

def dfs(now,x,y):
    visited.add(now)
    ans[now] = [x,y]
    for next in path[now]:
        if next[0] not in visited:
            dfs(next[0],next[1] + x,next[2] + y)


dfs(1,0,0)

for i in ans[1:]:
    if i == "undecidable":print(i)
    else: print(*i)
