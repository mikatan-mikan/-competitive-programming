n,m,l = map(int,input().split())

a = list(map(int,input().split()))#主菜
b = list(map(int,input().split()))#副菜
a_d = {a[i]:i + 1 for i in range(n)}#元々どこにあったかを保持
b_d = {b[i]:i + 1 for i in range(m)}
a_c = a.copy()
b_c = b.copy()
a.sort(reverse=True)#これの先頭から見る
b.sort(reverse=True)#(先頭の時点で選択するものが決まればそれ以降は見なくてよい)

#禁止されているものを受け取る
l_l = set([tuple(map(int,input().split())) for _ in range(l)])

ans = 0#答えを初期値0としてセット

#主菜を順にみる
for i in range(1,n + 1):
    #相手の副菜(高々10**5回しかまわらない)
    # -> breakしないのはl_lに含まれるときでその組み合わせは最大10*5しかないため
    for j in range(1,m + 1):
        if (a_d[a[i - 1]],b_d[b[j - 1]]) in l_l:#その組み合わせが違反しているなら次の副菜で試す
            continue
        else:
            #違反していないのであれば現在選んでいる主菜と副菜の合計額で更新or維持
            ans = max(ans,a[i - 1] + b[j - 1])
            break#主菜を固定したときの最大の副菜を選んでいるので以降の副菜には興味ない
print(ans)#最後に残った組み合わせの金額