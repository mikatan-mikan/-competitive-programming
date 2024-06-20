n = int(input())
a = list(map(int,input().split()))

#10**9(1-10桁程度しか存在しないのでそれぞれのけたが何個存在しているのかを調べる)
a_digit = {i:0 for i in range(1,11)}

for i in a:
    a_digit[len(str(i))] += 1

#iになる回数 = a[n - 1]を除いて1回
#jになる回数 = place 回

ans = 0

for i in range(len(a)):
    #iについての加算
    if i < len(a) - 1:
        #自分自身をよける
        a_digit[len(str(a[i]))] -= 1
        for key in a_digit:
            #その桁数の存在数 * (桁数 + 1) * 自分自身[その上に引っ付くので]
            ans += a_digit[key] * (10 ** (key)) * a[i]
            ans %= 998244353
    #jについての加算
    #単に自分自身を回数分加算すればよい
    ans += i * a[i]
    ans %= 998244353

print(ans)