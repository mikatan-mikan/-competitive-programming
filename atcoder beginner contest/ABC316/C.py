n,m = map(int,input().split())

from collections import deque

path = [deque() for _ in range(n+1)]

for i in range(m):
    a,b,c = map(int,input().split())
    path[a].append((b,c))
    path[b].append((a,c))

max_length = 0

def dfs(now,length,f_visited :set):
    global max_length
    if max_length < length:
        max_length = length
    f_visited.add(now)
    for next in path[now]:
        if next[0] not in f_visited:
            dfs(next[0],length + next[1],f_visited.copy())

for i in range(1,n+1):
    dfs(i,0,set())

print(max_length)