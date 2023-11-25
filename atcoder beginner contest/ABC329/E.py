n,m = map(int,input().split())

s = input()
t = input()
x = ["#" for _ in range(n)]

tpl = 0

do = set()#既に試した場所
isb = False

#実際に前から試せばよい
now_char_pl = 0
grace = 0#全回文字が一致した分だけ上書きしながら書くことができる
slide = 0
while True:
    #最初にsのどこまでとtのどこまでが一致しているかをチェックする
    tpl = -slide
    fir_tpl = -slide
    tpl_count = 0
    while True:
        for i in range(m):
            if i + now_char_pl >= n:
                isb = True
                break
            #文字が一致している又は破棄してよい文字なら
            if s[i + now_char_pl] == t[i] or x[i + now_char_pl] != "#":
                tpl += 1
            else:
                break
        #0文字でなければbreak,0文字以下ならnow_char_plを最大bef_tmp - 1だけ戻しながら再試行
        if tpl <= 0:
            do.add(now_char_pl)
            now_char_pl += 1
            grace -= 1
            if grace < 0:
                #猶予が無くなっても書くチャンスが残されていないなら失敗
                print("No")
                exit()
            slide -= 1
            tpl_count += 1
            tpl = fir_tpl + tpl_count
        else:
            break
    if isb:
        break

    #tpl番目までをその文字に置き換えればよい
    for i in range(tpl):
        #必要ないが分かりやすいので書き込む
        x[now_char_pl + i + slide] = t[i + slide]
    do.add(now_char_pl)
    #もしも今回すべての文字を使って終了していたら次回は前の任意文字を消して書くことができる
    if i + slide == m - 1:
        now_char_pl += 1
        slide = tpl - 1
        grace = tpl
    else:
        now_char_pl += tpl
        slide = 0
        grace = 0

print("Yes")