from sys import stdin
input = stdin.readline

n,q = map(int,input().split())

from collections import deque

part = deque([i + 1,0] for i in range(n))
query = [list(input().split()) for _ in range(q)]

dir = {"U":[0,1],"D":[0,-1],"L":[-1,0],"R":[1,0]}

for i in query:
    if int(i[0]) == 1:
        l = part[0]
        part.appendleft([l[0] + dir[i[1]][0],l[1] + dir[i[1]][1]])
    else:
        print(*part[int(i[1]) - 1])

