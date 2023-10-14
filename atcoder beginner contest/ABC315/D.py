h,w = map(int,input().split())

area = [list(input()) for _ in range(h)]



for p in range(2000):
    del_h = set()#消す行を保管
    del_w = set()#消す列を保管
    h_i = 0#現在見ている行
    w_i = 0#現在見ている列
    while True:
        if h_i < h - 1 and w_i < w - 1:
            if area[h_i][w_i] == area[h_i + 1][w_i] or area[h_i][w_i] == area[h_i][w_i + 1]:
                pass
            else:#消える事があり得ないなら
                h_i += 1
                w_i += 1
                continue

        #最初に行を見て、削除対象なら保管(オーバーしているなら無視)
        if h_i > h - 1:
            pass
        else:
            leng = 0
            watch = area[h_i][w_i]
            if w_i < w - 1:
                watch = area[h_i][w_i + 1]
            if area[h_i][w_i] == watch:
                leng += 1
                if h_i >=1:
                    if area[h_i - 1][w_i] == watch:
                        leng += 1
            for i in range(w_i + 1,w):#削除終了した場所から最後までを見る
                if area[h_i][i] == watch:
                    leng += 1
                else:
                    leng = 0
                    break
            if leng >= 2:
                del_h.add(h_i)
        #次に列を見て、削除対象なら保管(オーバーしているなら無視)
        if w_i > w - 1:
            pass
        else:
            leng = 0
            watch = area[h_i][w_i]
            if h_i < h - 1:#既に消えているなら視点を移す
                watch = area[h_i + 1][w_i]
            if area[h_i][w_i] == watch:
                leng += 1
                if w_i >=1:
                    if area[h_i][w_i - 1] == watch:
                        leng += 1
            for i in range(h_i + 1,h):#削除終了した場所から最後までを見る
                if area[i][w_i] == watch:
                    leng += 1
                else:
                    leng = 0
                    break
            if leng >= 2:
                del_w.add(w_i)

        if h_i == h - 1 and w_i == w - 1:
            break
        if h_i < h - 1:
            h_i += 1
        if w_i < w - 1:
            w_i += 1
    for i in sorted(list(del_h),reverse=True):
        del area[i]
        h -= 1
    for i in sorted(list(del_w),reverse=True):
        w -= 1
        for j in range(h):
            del area[j][i]

ans = h * w

print(ans)