import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n,m = map(int,input().split())

a = list(map(int,input().split()))

from collections import deque

path = [deque() for _ in range(n+1)]
vertex_max = [0] * (n + 1)

for i in range(m):
    u,v = map(int,input().split())
    path[u].append(v)
    path[v].append(u)

visited = set()
score_visited = {}
max_score = 0

def dfs(now):
    #現在地点におけるmaxを更新
    vertex_max[now] = len(score_visited)
    global max_score
    visited.add(now)
    if a[now - 1] in score_visited:
        score_visited[a[now - 1]] += 1
    else:
        score_visited[a[now - 1]] = 1
    for i in path[now]:
        if i in visited or a[i - 1] < a[now - 1] or len(score_visited) < vertex_max[i]:#もう訪問済みor 選んだところより現在の方が大きいならor vertex_max[i]に現時点で負けているなら
            continue
        if i == n:#ゴール地点についたなら
            if a[i - 1] in score_visited:
                score_visited[a[i - 1]] += 1
            else:
                score_visited[a[i - 1]] = 1
            max_score = max(max_score,len(score_visited))
            score_visited[a[i - 1]] -= 1
            if score_visited[a[i - 1]] == 0:
                score_visited.pop(a[i - 1])
            continue
        dfs(i)
        if i in visited:
            visited.remove(i)
        if a[i - 1] in score_visited:
            score_visited[a[i - 1]] -= 1
            if score_visited[a[i - 1]] == 0:
                score_visited.pop(a[i - 1])


dfs(1)

print(max_score)