
from collections import deque


N = int(input())

P = list(map(int,input().split()))

pin = 0
for i in range(len(P) - 1,-1,-1):
    #まず自分より小さい桁を探す ->その中で最も大きい数字とswapする
    num = []
    for j in range(len(P)):#p(j)からp(i)を見る
        if i > j:
            continue
        if P[i] > P[j]:
            num.append([P[j],i,j])#i桁目にp[j]より小さい数字があることを記憶
    num = sorted(num)
    try:
        P[num[-1][1]] , P[num[-1][2]] = P[num[-1][2]] , P[num[-1][1]]
        pin = num[-1][1]#i桁目以降を以後触る
        break#ひとまず最上位桁決定
    except:continue

#残りのけたをソート
back = P[pin + 1:]
back = sorted(back)
back.reverse()
P = P[0:pin + 1] + back


print(*P)
