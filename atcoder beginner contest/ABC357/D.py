n = int(input())

a = list(map(int,input().split()))

visited = set()
local_visited = set()
root = 0
save = {}

now = 0


def search_root(place,depth):
    global root,visited,local_visited,now
    #ここの結果が求まっているなら
    if place in save:
        return save[place]
    #パスが途絶えるまで見続ける
    if a[place - 1] not in visited:
        return search_root(a[place - 1],depth + 1) + 1
    else:
        return depth#結果的にはiから伸びている頂点の数(iを含む)

from collections import deque

ans = 0

for i in range(n):
    now = 0
    local_visited = set()
    c = search_root(i + 1,1)
    save[i + 1] = c
    #rootからつながっているすべての頂点を探索する
    #1..root - 1までの総和をO(1)で
    ans += (root - 1) * root // 2


print(ans)