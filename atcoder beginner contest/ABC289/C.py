N,M = map(int,input().split())

a = []

from itertools import combinations

for i in range(M):
    input()#cが不必要なので破棄
    a.append(set(map(int,input().split())))

cnt = 0
item = set()
for i in range(1,M + 1):
    for j in combinations(a,i):
        item.clear()
        for k in range(len(j)):
            item = item | j[k]
        if len(item) == N:
            cnt += 1
print(cnt)