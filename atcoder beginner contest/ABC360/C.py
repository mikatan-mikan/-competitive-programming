n = int(input())

a = list(map(int, input().split()))
w = list(map(int, input().split()))

from collections import deque
from sortedcontainers import SortedList

box = [SortedList() for _ in range(n + 1)]

for i in range(n):
    box[a[i]].add(w[i])#箱に重さを入れる

#空の箱を管理
space = deque()
for i in range(n):
    if len(box[i + 1]) == 0:
        space.append(i + 1)

cost = 0

for i in range(1,n + 1):#箱を順にみる
    #模試からなら
    if len(box[i]) == 0:
        continue
    else:
        #箱の長さが2以上の時繰り返す
        while len(box[i]) >= 2:
            #先端を抜き出す
            first = box[i].pop(0)
            box[space[0]].add(first)
            space.popleft()
            cost += first

print(cost)
