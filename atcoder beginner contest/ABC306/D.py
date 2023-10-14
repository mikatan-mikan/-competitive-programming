N = int(input())

dp = [[0 for _ in range(N + 1)] for _ in range(2)]


for i in range(1,N + 1):
    x,y = map(int,input().split()) # x = 0なら解毒,x = 1なら毒 y = おいしさ
    if x == 0: #解毒なら
        dp[0][i] = max(max(dp[0][i - 1],dp[1][i - 1]) + y,dp[0][i - 1]) #食べて元々毒だった場合と毒でなかった場合、食べなかった場合の比較
        dp[1][i] = dp[1][i - 1] #食べなくてもともと毒なら
    else: #毒なら
        dp[0][i] = dp[0][i - 1] #食べなくて元々毒でない場合
        dp[1][i] = max(dp[0][i - 1] + y,dp[1][i - 1]) #食べて元々毒でなかった場合

print(max(dp[0][-1],dp[1][-1]))