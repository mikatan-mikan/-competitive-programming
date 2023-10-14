n,m = map(int,input().split())
 
sell = list(map(int,input().split()))#売る人
buy = list(map(int,input().split()))#買う人
 
buy.sort(reverse=True)
sell.sort()
 
x = 0#現在の価格
 
pl_b = m - 1#buyerを見た場所
pl_s = 0#sellerを見た場所
 
def out(x):
        print(x)
        exit()

while True:
    #これ以上なら売ってくれる
    x = sell[pl_s]#これが買いたい人より多ければいい(pl_b + 1人より)
    while True:
        if pl_s < n - 1:
            if sell[pl_s + 1] != x:
                break
            else:
                pl_s += 1
        else:
            break
    while True:
        if x > buy[pl_b] and pl_b >= 0:
            pl_b -= 1
        else:
            break
    if pl_s >= pl_b:
        if pl_b < 0:
            x = min(buy[0] + 1,x)
        print(x)
        exit()
    pl_s += 1 if pl_s < n - 1 else out(buy[0] + 1)