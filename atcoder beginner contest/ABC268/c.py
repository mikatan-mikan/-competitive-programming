from collections import deque


N = int(input())
p = list(map(int,input().split()))

ans = deque()

range_loop = list(range(N))

for i in range(1,N + 1,2):
    cnt = 0
    for j in range_loop: 
        if p[j] == ((j + i) % N) or p[j] == ((j + i + 1) % N) or p[j] == ((j + i - 1) % N):cnt += 1
    ans.append(cnt)

print(max(ans))