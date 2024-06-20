import itertools
from collections import deque


N = int(input())

P = deque(map(int,input().split()))

all = list(itertools.permutations(sorted(P.copy()), N))

for i in range(len(all)):
    # print(all[i],type(all[i]),tuple(P),type(tuple([P])))
    if all[i] == tuple(P):
        print(*all[i - 1])