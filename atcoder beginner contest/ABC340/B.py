q = int(input())

from collections import deque

a = deque()

for i in range(q):
    num,in_ = map(int,input().split())
    if num == 1:
        a.append(in_)
    else:
        print(a[-in_])