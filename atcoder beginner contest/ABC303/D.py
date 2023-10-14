X,Y,Z = map(int,input().split())

S = input()

FLG = [False,False] # a,A
num = 0

cpl = False# capslock

next_set = []
sum_time = [0]
fast_i = [-1 for _ in range(len(S))]
now = 0
i = 0

while True:
    try: S[i]
    except: 
        now += 1
        try: sum_time[now]
        except: break
        cpl = next_set[now - 1][1]
        i = next_set[now - 1][0]
    if S[i] == 'a':
        FLG[0] = True
        num += 1
        while True:
            i += 1
            try: S[i]
            except: break
            if S[i] == 'a':
                num += 1
            else:
                break
    elif S[i] == 'A':
        FLG[1] = True
        num += 1
        while True:
            i += 1
            try: S[i]
            except: break
            if S[i] == 'A':
                num += 1
            else:
                break
    if FLG[0]:
        FLG[0] = False
        if cpl: # capslockが使われているなら
            pln1 = num * Y
            pln2 = Z + num * X
        else: # 使われていないなら使って押した場合の時間
            pln1 = num * X
            pln2 = Z + num * Y
        if pln1 == pln2:
            #分岐パターン保持
            next_set.append([i,not cpl])
            sum_time.append(sum_time[now] + pln2)

            sum_time[now] += pln1
        elif pln1 < pln2:
            sum_time[now] += pln1
        else:
            cpl = True
            sum_time[now] += pln2
        num = 0
    else:
        FLG[1] = False
        if cpl == False:
            pln1 = num * Y
            pln2 = Z + num * X
        else:
            pln1 = num * X
            pln2 = Z + num * Y
        if pln1 == pln2:
            #分岐パターン保持
            next_set.append([i,not cpl])
            sum_time.append(sum_time[now] + pln2)

            sum_time[now] += pln1
        elif pln1 < pln2:
            sum_time[now] += pln1
        else:
            cpl = False
            sum_time[now] += pln2
        num = 0

print(min(sum_time))