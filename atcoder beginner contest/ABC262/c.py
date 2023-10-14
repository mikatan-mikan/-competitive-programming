
from collections import deque
from itertools import combinations
N = int(input())

A_ = list(map(int,input().split()))

A = deque()
for i in range(N):
    A.append([A_[i],i + 1])

cnt = 0

for i in combinations(A,2):
    if i[0][1] < i[1][1]:
        if i[0][1] == min(i[0][0],i[1][0]):
            if i[1][1] == max(i[0][0],i[1][0]):
                cnt += 1
    else:
        if i[0][1] == max(i[0][0],i[1][1]):
            if i[1][1] == min(i[0][0],i[1][0]):
                cnt += 1

print(cnt)