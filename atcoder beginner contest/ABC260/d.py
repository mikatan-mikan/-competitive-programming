from collections import deque


N,K = map(int,input().split())

P = list(map(int,input().split()))

field = set()

for i in range(N):
    if P[i] not in field:
        field.append(P[i])
    
a = {"a":9,"v":4}

a["a"] = 9
a["v"] = 4
a[1] = 4