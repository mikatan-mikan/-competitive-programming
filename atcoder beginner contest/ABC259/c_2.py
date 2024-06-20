S = input()

T = input()
S_flag = False
T_flag = False
s_add = 0#見る場所のカウンター
t_add = 0
target = S[0]#最初の文字
streak = 0

while True:
    try:#ここで引っかかる=最後まで進んだ
        S[s_add]
        T[t_add]
    except:
        break
    if S[s_add] == T[t_add]:#同じなら
        if s_add >= 1:
            if S[s_add] != S[s_add - 1]:
                streak = 0
        streak += 1
        s_add += 1
        t_add += 1
        continue
    else:#もし違った場合
        if s_add == t_add and t_add == 0:#一回目で違うなら
            print("No")
            exit()
        if S[s_add] != S[s_add - 1] and T[t_add] != T[t_add - 1] and S[s_add] != T[t_add]:#両方とも前回の文字と変わってかつ文字が一致しないなら
            print("No")
            exit()
        if S[s_add] != S[s_add - 1]:#Sが変わったら
            if streak <= 1:
                print("No")
                exit()
            while True:
                t_add += 1#t_addを次の文字になるまで変更
                if T[t_add] == T[t_add - 1]:
                    continue
                streak = 0
                break#もしTが変わったらまた判定に戻る
        elif T[t_add] != T[t_add - 1]:#Tが変わった場合
            print("No")
            exit()
        #     while True:
        #         s_add += 1#s_addを次の文字になるまで変更
        #         if S[s_add] == S[s_add - 1]:
        #             continue
        #         streak = 0
        #         break#もしSが変わったらまた判定に戻る

if len(T) - (t_add + 1) > 0:#Tがまだ残っていたら
    for i in range(len(T) - (t_add + 1)):
        if T[t_add + (i + 1)] == T[t_add + i]:
            continue
        else:
            print("No")
            exit()
elif len(S) - (s_add + 1) > 0:
    for i in range(len(S) - (s_add + 1)):
        if S[s_add + (i + 1)] == S[t_add + i]:
            continue
        else:
            print("No")
            exit()

print("Yes")