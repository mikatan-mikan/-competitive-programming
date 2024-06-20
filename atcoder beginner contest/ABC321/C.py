k = int(input())

now = 0#10桁



#1桁ずつ上から見た時にk番目の狭義単調減少の数字を探す
for j in range(k):
    bef = now
    now += 1
    #狭義単調減少の文字列なら(nowの桁数回)
    if len(str(now)) == 1:
        continue
    for i in range(len(str(now)) - 1):
        if (now // (10 ** i)) % 10 >= (now // (10 ** (i + 1))) % 10:
            print((now // (10 ** i)) % 10,(now // (10 ** (i + 1))) % 10)
            #次の狭義単調減少を求めるnowの桁数回繰り返す
            for l in range(i + 1,0 - 1,-1):
                #問題のある桁を見てその桁にも1加算し、その後その前の桁でも+1する
                #(nowのl桁目に1加算)
                if (now // 10 ** l) % 10 <= (now // 10 ** (l + 1)) % 10:
                    now_l = now // 10 ** (l + 1)
                    now = now_l + 1 
                    now *= 10 ** (l + 1)
            now = list(str(now))
            now[i] = str(len(now) - (i - 1))
            now = int("".join(now))

print(now)