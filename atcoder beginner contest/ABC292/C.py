# DFSすればO(N)?

from collections import deque

N,M = map(int,input().split())

path = deque([deque() for _ in range(N + 1)])
cnt = deque([0 for _ in range(N + 1)]) # 訪れた回数を記録
visited = set()

def dfs(place,bef):
    global visited , dot_num , visited_ttime
    visited_ttime.add(place)
    visited.add(place)
    dot_num += 1
    for next_place in path[place]:
        if next_place == bef:
            continue
        # 既に移動済みであったとしてもそこにpathは存在しているのでカウントする
        if next_place not in visited:
            dfs(next_place,place)



for i in range(M):
    to,to_2 = map(int,input().split())
    path[to].append(to_2)
    path[to_2].append(to)

for item in range(len(path)):
    # itemの中身をまわす
    for i in path[item]:
        # iが未探索なら
        if i not in visited:
            # visited.add(item)
            path_num , dot_num = 0 , 0
            if i != item: dot_num = 1
            visited_ttime = set([item])
            visited.add(item)
            dfs(i,item)
            # ここでvisited_ttimeの中にある要素を数えて2で割る
            for j in visited_ttime:
                path_num += len(path[j])
            if (path_num / 2) != dot_num:
                print("No")
                exit()

print("Yes")