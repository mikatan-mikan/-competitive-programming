N,A,B = map(int,input().split())
X = input()



def make_palindrome(X, A, B):
    n = len(X)
    dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for i in range(n+1):
        for j in range(n+1):
            if i == 0:
                dp[i][j] = j * B
            elif j == 0:
                dp[i][j] = i * B
            elif X[i-1] == X[n-j]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j] + A, dp[i][j-1] + B)
    return dp[n][n]

print(make_palindrome(X,A,B))