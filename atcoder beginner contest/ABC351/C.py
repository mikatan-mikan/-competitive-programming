n = int(input())
        
a = list(map(int,input().split()))

from collections import deque

que = deque()

for i in a:
    if len(que) <= 0:
        que.append(i)
        continue
    back = que[-1]
    que.append(i)
    if back != i:
        continue
    while True:
        if len(que) <= 1:
            break
        elif que[-2] != que[-1]:
            break
        else:
            que.pop()
            que.append(que.pop() + 1)



print(len(que))

