from collections import deque

N = int(input())

A = list(map(int,input().split()))

ref_a = 0
sleep = 1

sleep_time = deque([0])

for i in range(A[-1]):
    if A[ref_a] == i:
        ref_a += 1
        sleep = 1 - sleep
    if sleep == 1:
        sleep_time.append(sleep_time[-1] + 1)
    else:
        sleep_time.append(sleep_time[-1])


Q = int(input())


for i in range(Q):
    r,l = map(int,input().split())
    print(sleep_time[l] - sleep_time[r])

