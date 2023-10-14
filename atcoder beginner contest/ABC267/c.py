from collections import deque


N , M = map(int,input().split())

A = list(map(int,input().split()))

ans_tmp = deque()

for i in range(N - M + 1):#ここでB1-Bmが取れる範囲に応じてループ
    ans = [j * A[i+(j-1)] for j in len(A[i : i + M])]
    ans_tmp.append(sum(ans))

print(max(ans_tmp))
