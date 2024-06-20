n,k = map(int,input().split())

c_ = list()
v_ = list()

for i in range(n):
    c,v = map(int,input().split())
    if i != 0 :
        if c == c_[-1]:
            if v > v_[-1]:
                v_[-1] = v
            k -= 1
            continue
    c_.append(c)
    v_.append(v)


if k == 0:
    ans = sum(v_)
elif k < 0:
    ans = -1
else:
    #残っている分を取り除く必要がある。
    #但し取り除いた際、隣り合うことが発生してはならない
    dp = [[0 for _ in range(k + 1)] for i in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            # 色を選択しない場合
            dp[i][j] = max(dp[i][j], dp[i - 1][j])
            # 色を選択する場合
            if i > 1 and c_[i - 1] == c_[i - 2]:
                dp[i][j] = max(dp[i][j], dp[i - 2][j - 1] + v_[i - 1])
            else:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + v_[i - 1])

    ans = dp[n][k]

print(ans)