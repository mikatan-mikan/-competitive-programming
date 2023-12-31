n = int(input())

from collections import deque

p_1 = deque([0])
p_2 = deque([0])

for i in range(n):
    c,p = map(int,input().split())
    p_1.append(p_1[-1] + (p if c == 1 else 0))
    p_2.append(p_2[-1] + (p if c == 2 else 0))

for q in range(int(input())):
    l,r = map(int,input().split())
    print(p_1[r] - p_1[l - 1],p_2[r] - p_2[l - 1])