#deque 
from collections import deque

N,M = map(int,input().split())

A_list : list = [list(map(int,input().split())) for _ in range(M)]
discord = deque([[i for i in range(1,N + 1)] for _ in range(N + 1)])# N番目の人は1 ~ N番目の人と不仲の可能性がある

for i in range(1,N + 1):#不仲listから自身を抜く
    discord[i].remove(i)

for A in A_list:# Aの中を順にみていく
    for i in range(N + 1):
        if i != 0:# 最初の人以外は
            # 自身が不仲である可能性のある人からA[i - 1]を削除
            try:
                discord[A[i]].remove(A[i - 1])
            except:pass
        if i != N - 1:# 最後の人以外は
            # 自身が不仲である可能性のある人からA[i + 1]を削除
            try: discord[A[i]].remove(A[i + 1])
            except:pass

#不仲な組みを計算
sum = 0
del discord[0]
for i in range(N):
    sum += len(discord[i])

print(sum // 2)