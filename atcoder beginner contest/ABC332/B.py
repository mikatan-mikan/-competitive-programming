k,g,m = map(int,input().split())

now_g,now_m = 0,0

for i in range(k):
    #gがいっぱいなら
    if now_g == g:
        now_g = 0#捨てる
    elif now_m == 0:#マグカップが空
        now_m = m#マグカップを満たす
    else:#そうでないなら
        if g - now_g <= now_m:#グラスを満たせる場合
            now_m -= g - now_g
            now_g = g
        else:#満たせないなら全て移す
            now_g += now_m
            now_m = 0

print(now_g,now_m)