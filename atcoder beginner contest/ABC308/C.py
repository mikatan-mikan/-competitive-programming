from collections import deque
from fractions import Fraction

n = int(input())
p = deque()

for i in range(1, n + 1):
    a,b = map(Fraction,input().split())
    p.append([a/(a + b),i])

p = sorted(p,key = lambda x:(-x[0],x[1]))


for i in p:
    print(i[1],end=" ")
