n,m = map(int,input().split())

from collections import deque

from sortedcontainers import SortedDict

path = SortedDict()
can_visit = set()

for i in range(m):
    k,c = map(int,input().split())
    a = set(map(int,input().split()))
    #cが存在するか
    if c in path:
        path[c] |= a
    else:
        path[c] = a
    can_visit |= a

#連結でない
if len(can_visit) != n:
    print(-1)
    exit()

cost = 0
can_visit = set()
list_ = []
#最短経路を求める
for key in path:
    now_len = len(can_visit)
    can_visit |= path[key]
    #もし0であれば、集合を結合している可能性がある。
    if len(can_visit) == now_len:
        if len(list_) != 1:
            del_list = deque()
            for i in range(len(list_) - 1):
                for j in range(i + 1,len(list_)):
                    if path[key] | list_[i] | list_[j] != len(list_[i]) + len(list_[j]):
                        list_[j] |= list_[i]
                        del_list.append(i)
                        cost += key
            for i in del_list:
                del list_[i]
        continue

    cost += key * (len(can_visit) - now_len)
    #独立した集合をすべて持っていく場合
    if len(can_visit) - now_len == len(path[key]):
        cost -= key
        list_.append(path[key])

if len(list_) > 1:
    print(-1)
    exit()
print(cost)