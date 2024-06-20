from collections import deque


N , M = map(int,input().split())

A = list(map(int,input().split()))

ans_tmp = deque()
##順番が自由でいいなら逆順にソートされた配列が最も最適なはず
A.sort()

ans_tmp = A[-M:]
ans = 0
for i in range(len(ans_tmp)):
    ans += (i + 1) * ans_tmp[i]

print(ans)
