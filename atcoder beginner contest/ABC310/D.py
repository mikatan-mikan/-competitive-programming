n,t,m = map(int,input().split())

path = [list(map(int,input().split())) for _ in range(n)]

num = 0
p = n

from operator import mul
from functools import reduce

def cmb(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under

for j in range(1, n - t + 1):#全体の人数からチーム数をひいた数(1チームが最大限保有できる人数まで)
    num += 