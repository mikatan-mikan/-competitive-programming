t = input() + "0000000000"
n = int(input())

#今までの状態100に対してすべて操作を行う。
#つまり、現在の袋の中にある文字列(max:10)をすべての状態について適応できるか調査し、できる場合は置き換える(なおこの際、それより後の数字は変更しない(その後の数字は自分自身より過去の袋の結果のため))
#計算量はn * Ai * len(T) * len(Si)程度で最大100*10*100*10 = 10 ** 6

#状態を初期化(10**9なら到達していない)
condition = {i:10**9 for i in range(len(t) + 1)}
condition[0] = 0#0文字目を0に
condition_now = condition.copy()

for i in range(n):
    a_s = list(map(str,input().split()))
    #今回のa_sにおいて既に更新した場所を記録する
    #例えば時間=2に3番を更新した後、時間=2にさらに3からの部分を更新してしまうと不整合が起こる。
    his = set()
    for j in range(int(a_s[0])):#sの中身を見る
        now_str = a_s[j + 1]#今見る文字
        for k in range(len(t) - 10):#全ての状態に対して
            if condition[k] != 10**9:#そこまで到達済みであればそこからそれ以降まで現在の文字列を使って伸ばしたとき、最小値を更新できれば更新する
                can_use = True
                for l in range(len(now_str)):
                    if t[k + l] != now_str[l]: 
                        can_use = False
                        break#条件を満たさない
                if can_use:
                    #現在の状態から進めた場所のスコアが現状と更新後のどちらがよいかを決定
                    #この際now側を更新することで"時間=2に3番を更新した後、時間=2にさらに3からの部分を更新してしまうと不整合が起こる"ようなことを避ける
                    #さらにcondition_nowが更新された後同じ時刻に同じ場所のcondition_nowが変更されることもないこともないはずなので、condition_now自身もminに含める
                    condition_now[k + len(now_str)] = min(condition[k + len(now_str)],condition[k] + 1,condition_now[k + len(now_str)])
    condition = condition_now.copy()

print(condition[len(t) - 10] if condition[len(t) - 10] != 10**9 else -1)