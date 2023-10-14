n,x,f,s = map(int,input().split())

#コード行数,今回書いたコード数

dp = [[[0,0] for _ in range(10 ** 5)] for _ in range(2)]

dp[0][0][1] = x + f

time = 0

while True:
    time += 1
    minus_code = dp[0][time - 1][1] - f if dp[0][time - 1][1] - f > 0 else 0
    plus_code = dp[1][time - 3][1] + s if dp[1][time - 3][1] + s <= x else x
    #前回が稼働していて、今回も稼働していた場合のコード行数と前回まで寝ていてその状態のコードに加算した結果
    #連続稼働の方がよかった場合
    if dp[0][time - 1][0] + minus_code >= dp[1][time - 3][0] + plus_code:
        #コードを加算して
        dp[0][time][0] = dp[0][time - 1][0] + (minus_code)
        #今回書いた出来るコード領を減算する
        dp[0][time][1] = minus_code
    else:
        #コードを減算して
        dp[0][time][0] = dp[1][time - 3][0] + (plus_code)
        #今回書いたコード領を加算する
        dp[0][time][1] = plus_code
    dp[1][time] = dp[0][time - 1]
    if dp[0][time][0] >= n:
        break


print(time)
