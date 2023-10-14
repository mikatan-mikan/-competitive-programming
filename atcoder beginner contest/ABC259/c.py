S = input()

T = input()
S_flag = False
T_flag = False
s_add = 0
t_add = 0
target = S[0]#最初の文字
for i in range(max(len(S),len(T))):
    s_i,t_i = i + s_add,i + t_add
    if S_Flag == True:#もしSを飛ばすなら
        if S[s_i] == target:#次の文字もまだ同じなら
            continue#さらに次へ
        target = S[s_i]#そうでなければ新しい文字をセット
        S_Flag = False#フラグ削除
        if target != T[t_i]:
            
    if T_flag == True:
        if T[t_i] == target:#次の文字もまだ同じなら
            continue#さらに次へ
        target = T[t_i]#そうでなければ新しい文字をセット
        T_Flag = False#フラグ削除
    if target != T[t_i] and i == 0:#最初から違う場合
        print("No")
        exit()
    if target == T[t_i] and target == S[s_i]:#まだ互いに同じ文字なら
        continue
    elif target != T[t_i] and target != S[s_i]:#両方が違うなら
        if T[t_i] != S[s_i]:
            print("No")
        target = S[s_i]
    elif target != T[t_i]:#Tだけが違うなら
        S_flag = True#Sを次の文字まで飛ばす
    elif target != S[s_i]:#Sだけ違うなら
        T_flag = True#Tを次の文字まで飛ばす