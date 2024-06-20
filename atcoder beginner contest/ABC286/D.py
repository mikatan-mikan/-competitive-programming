#Xが鞄の容量
#Aが重さ



N,X = map(int,input().split())#X円払えればいい

A = [0] * 101#i円がA[i]枚

for i in range(N):
    a,b = map(int,input().split())
    A[a] = b

#合計枚数
sum_coins = sum(A)

#立てにコインを入れたか,横に合計金額
dp = [[0] * (X + 1) for _ in range(sum_coins)]

coin_range = list(range(1,101))
coin_range.reverse()#高いものを入れれるかを先に見る

for i in range(1,X + 1):#1円からX円まで
    for j in coin_range:#j円硬貨を入れる/入れない
        if A[j] > 0 and i >= dp[i - 1] + j:#コインが存在して前回までの結果ににj円足しても入れることが可能なら
            dp[i] = dp[i - 1] + j
            break
    if dp[i] == 0:
        dp[i] = dp[i - 1]


print(dp)