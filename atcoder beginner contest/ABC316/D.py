n = int(input())

from collections import deque
x,y,z = deque(),deque(),deque()

win = 0
lose = 0

for i in range(n):
    in_ = list(map(int,input().split()))
    if x > y:
        win += in_[2]
    else:
        lose += in_[2]
        x.append(in_[0])
        y.append(in_[1])
        z.append(in_[2])

if win > lose:
    print(0)

under = win - lose
dp = [[0] * (n+1) for _ in range(under + 2)]
dp_mem = [[0] * (n+1) for _ in range(under + 2)]

#不足者数
dp[0][0] = 10**9
none = under

for i in range(1,under + 1):#何人の候補者が必要か
    for j in range(1,n + 1):#どこの選挙区までを見たか
        if dp[i][j - 1] < dp[i - z[i - 1]][j - 1] + (x[i - 1] - y[i - 1]) and dp_mem[i][j - 1] :#前の選挙区の答え or 現在の候補者数から現在の選挙区の候補者数を差し引いて(i - z[i - 1])そこに今回の選挙区の候補者数を足す
            dp[i][j] = dp[i][j - 1]
            dp_mem[i][j] += dp_mem[i][j - 1]
        else:
            dp[i][j] = dp[i - z[i - 1]][j - 1] + (x[i - 1] - y[i - 1])
            dp_mem[i][j] += dp_mem[i - z[i - 1]][j - 1] + z[i - 1]

    