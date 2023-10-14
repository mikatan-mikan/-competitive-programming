MOD = 998244353

def count_valid_parentheses(S):
    N = len(S)
    x = S.count('?')
    dp = [[0] * (x + 1) for _ in range(N + 1)]

    # DPの初期化
    dp[0][0] = 1

    for i in range(1, N + 1):
        for j in range(x + 1):
            if S[i - 1] == '(' or S[i - 1] == ')':
                dp[i][j] = dp[i - 1][j]
            elif S[i - 1] == '?':
                dp[i][j] = (dp[i - 1][j - 1] * 2 + dp[i - 1][j]) % MOD

    return dp[N][x]

if __name__ == "__main__":
    S = input().strip()
    result = count_valid_parentheses(S)
    print(result)