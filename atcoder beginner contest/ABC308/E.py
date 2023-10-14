n = int(input())

a = list(map(int,input().split()))
s = input()

#0番目=そこでmを拾った場合
#1番目=そこでeを拾った場合
#2番目=そこでsを拾った場合
dp = [[0 for _ in range(n + 1)] for _ in range(3)]

for i in range(1,n + 1):
    dp[0][i] = dp[0][i - 1]
    dp[1][i] = dp[1][i - 1]
    dp[2][i] = dp[2][i - 1]
    if s[i - 1] == "M":
        dp[0][i] = max(dp[0][i], a[i - 1])
    elif s[i - 1] == "E":
        dp[1][i] = max(dp[1][i], a[i - 1])
    else:
        dp[2][i] = max(dp[2][i], a[i - 1])

print(dp[-1][-1])