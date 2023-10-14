from collections import deque
import sys

sys.setrecursionlimit(1000000000)

N = int(input())
A = list(map(int,input().split()))

ameba_list = deque()

for i in range(N):
    ameba_list.append(A[i])

a = [0,1]

a[0] = 0

def re_mod_2(num):
    global cnt
    num = A[int(num / 2) - 1]
    cnt += 1
    if num != 1: re_mod_2(num)

print(0)#一匹目
print(1)
print(1)
for i in range(1,N):
    cnt = 1
    re_mod_2(ameba_list[i])
    print(cnt)
    print(cnt)