##最初に辺を一つしか持たない部分を探してその後ループの存在回数分カウントする
import sys
from collections import deque
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline#入力高速化

N,M = map(int,input().split())

path = [deque() for _ in range(N + 1)]#path[i]=iからつながっている辺(dequeにしてみる)

visited = set()
cnt = 0

def dfs(place,bef):
    global visited,cnt
    # if place in visited:#訪問済みなら
    #     cnt += 1#閉路を削除する
    #     return
    visited.add(place)#現在地を探索済みに
    for next in path[place]:#つながっている場所を順に探索
        #もし行き先が来た元の場所ならスルー
        if next == bef:
            continue
        if next in visited:
            cnt += 1
            continue
        dfs(next,place)


for i in range(M):
    a,b = map(int,input().split())
    path[a].append(b)
    path[b].append(a)

for i in range(1,N + 1):
    if i not in visited:
        if len(path[i]) >= 1:#辺があればそこから始める(さらに未探索なところなら)
            dfs(i,None)
print(int(cnt / 2))

