import sys
from collections import deque
sys.setrecursionlimit(10**5)

N = int(input())
#はしご
Ladder = [sorted(deque(map(int,input().split()))) for _ in range(N)]

#深さ優先探索をするのでソートする(上の階から見るので逆順)
Ladder = sorted(Ladder)

max_floor = 1

tmp0_box = set()#後から行くかもしれない場所用
tmp1_box = set()
tmp_box = deque()
now_point = set([1])#いる可能性のある場所
for i in range(len(Ladder)):#幅優先
    if Ladder[i][0] in now_point:
        now_point.add(Ladder[i][1])
    elif Ladder[i][1] in now_point:
        now_point.add(Ladder[i][0])
    elif Ladder[i][0] in tmp0_box:
        for x in tmp_box:
            if x[0] == tmp_box[0]: 
                now_point.add(x[1])
    elif Ladder[i][1] in tmp1_box:
        for x in tmp_box:
            if x[1] == tmp_box[1]: 
                now_point.add(x[0])
    else:#今の時点で行けないなら
        tmp0_box.add(Ladder[i][0])
        tmp1_box.add(Ladder[i][1])
        tmp_box.append(Ladder)
    
print(max(now_point))