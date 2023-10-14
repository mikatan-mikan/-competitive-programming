#ABC 289 E
T = int(input())
for t in range(T):
    N,M = map(int,input().split())
    C = list(map(int,input().split()))
    D = list(map(int,input().split()))
    P = list(map(int,input().split()))
    dp = [[0]*(M+1) for _ in range(N+1)]
    for i in range(1,N+1):
        for j in range(1,M+1):
            dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + C[i-1]*D[j-1]
    print('#{} {}'.format(t+1,dp[N][M]))
