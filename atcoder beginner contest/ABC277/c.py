import sys
from collections import deque
sys.setrecursionlimit(2 *10**5)

N = int(input())
#はしご
Ladder = [sorted(deque(map(int,input().split()))) for _ in range(N)]

#深さ優先探索をするのでソートする
Ladder = sorted(Ladder)

max_floor = 1

def dfs(Ladder,floor):#base_floor = 元居た階(戻らないように)
    global max_floor
    for i in range(len(Ladder)):
        if floor in Ladder[i]:#現在のフロアより上につながっているladderがあれば
            if Ladder[i][1] != floor:
                if max_floor < Ladder[i][1]:#最大階を上回ったら書き換え
                    max_floor = Ladder[i][1]
                dfs(Ladder[:i] + Ladder[i + 1:],Ladder[i][1])
            else:
                dfs(Ladder[:i] + Ladder[i + 1:],Ladder[i][0])
        elif Ladder[i][0] > floor and Ladder[i][1] > floor:
            break


dfs(Ladder,1)
print(max_floor)