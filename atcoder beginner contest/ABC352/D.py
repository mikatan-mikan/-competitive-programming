n,k = map(int,input().split())
p = list(map(int,input().split()))
p_sort = [i for i in range(1,n + 1)]
#p[p_place[p_sort]]をもちいて座標変換
p_place = {p[i - 1]:i - 1 for i in range(1,n + 1)}

from sortedcontainers import SortedList
from collections import deque

now_group = SortedList()
now_group_num = deque()
#それぞれの距離に対するスコアを計算
for i in range(k - 1):
    now_group.add(p_place[p_sort[i]])
    now_group_num.append(p_sort[i])
score = [0 for _ in range(n)]

for i in range(k - 1,n):
    now_group.add(p_place[p_sort[i]])
    now_group_num.append(p_sort[i])
    score[i] = now_group[-1] - now_group[0]
    #now_group_numの先頭要素とそれに関するスコアを削除
    now_group.discard(p_place[now_group_num.popleft()])



print(min(score[k - 1:]))