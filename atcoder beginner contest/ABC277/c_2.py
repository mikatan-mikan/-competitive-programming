import sys
from collections import deque
sys.setrecursionlimit(10**5)

N = int(input())
#はしご
Ladder = [sorted(deque(map(int,input().split()))) for _ in range(N)]

#深さ優先探索をするのでソートする(上の階から見るので逆順)
Ladder = sorted(Ladder)
Ladder.reverse()

max_floor = 1

def dfs(Ladder,floor):
    global max_floor
    break_flag = False#2階を探索するときLadder[i][0]が1の時false2になるとtrue,true時にelseになる(探索階がもう出ないなら)とbreak
    for i in range(len(Ladder)):
        if Ladder[i][0] == floor:#現在のフロアより上につながっているladderがあれば
            break_flag = True
            if max_floor < Ladder[i][1]:#最大階を上回ったら書き換え
                max_floor = Ladder[i][1]
            dfs(Ladder[i:],Ladder[i][1])
        elif break_flag:
            break

for i in range(len(Ladder)):
    dfs(Ladder,Ladder[0][1])
print(max_floor)