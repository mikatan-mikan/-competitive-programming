n,m = map(int,input().split())

#dp[その台までの最大値][現在の最大金額]
#dp[今回の台][現在の最大金額] = max(dp[今回の台 - 1][現在の最大金額 - 一回分の金額] + 今回の期待値,dp[今回の台 - 1][現在の最大金額])

dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
dp_flg = [[False for _ in range(m+1)] for _ in range(n+1)]

dat = [list(map(int,input().split())) for _ in range(n)]

for i in range(1,n+1):
    for j in range(1,m+1):
        if dp[i][j] < m:
            if j >= dat[i-1][0]:
                dp[i][j] = max(dp[i-1][j],dp[i-1][j-dat[i-1][0]]+dat[i-1][1])
            else:
                dp[i][j] = dp[i-1][j]
