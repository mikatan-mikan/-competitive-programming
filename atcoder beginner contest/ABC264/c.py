H_1 , W_1 = map(int,input().split())
A = []
for _ in range(H_1):
    A.append(list(map(int,input().split())))
H_2 , W_2 = map(int,input().split())
B = []
for _ in range(H_2):
    B.append(list(map(int,input().split())))

if H_2 > H_1 or W_2 > W_1:
    print("No")
    exit()
ne_minus = 0

def delete_ma():
    global ne_minus,H_2 , W_2,H_1 , W_1,A,B
    #置いておく必要のないAの行を削除する
    del_list = []
    for k in range(len(A)):#Aの全行を見る
        de_cnt = 0
        for i in range(len(B)):#bの全行に対して(どれかの行に当てはまれば必要であるかもしれない)
            b_cnt = 0
            for l in range(len(A[k])):#それぞれの要素
                if B[i][b_cnt] == A[k][l]:#現在まだA[k]に見つかっていないB[i][b_cnt]があったらb_cntをたす
                    #最終的にb_cnt == len(B[i]) - 1なら全部ある
                    b_cnt += 1
                    if b_cnt == len(B[i]):
                        break
            #もしそれぞれの要素をBの全行で見てどのBの行にもできないなら消す
            if b_cnt == len(B[i]):
                continue#このまま次の行に続く
            else:
                de_cnt += 1
        if de_cnt == len(B):#Bのどの行にも使えないなら
            del_list.append(k)
    del_list.reverse()
    for i in del_list:
        del A[i]

    #次は縦方向に
    del_list = []
    for i in range(W_1 - ne_minus):#Aのi列目を見る
        de_cnt = 0
        for j in range(W_2):#Bのj列目
            b_cnt = 0
            for l in range(len(A)):#それぞれの行
                if B[b_cnt][j] == A[l][i]:
                    b_cnt += 1
                    if b_cnt == len(B):
                        break
            if b_cnt == len(B):
                continue
            else:
                de_cnt += 1
        if de_cnt == len(B[0]):
            del_list.append(i)
    ne_minus += len(del_list)
    del_list.reverse()
    a = list(range(len(A)))
    a.reverse()
    for i in a:
        for j in del_list:
            del A[i][j]

for i in range(10000):
    delete_ma()

del_list = []

for i in range(len(A)):
    A[i] = set(A[i])
for j in range(len(B)):
    B[j] = set(B[j])
A = list(map(list, set(map(tuple, A))))
B = list(map(list, set(map(tuple, B))))
if A == B:
    print("Yes")
else:
    print("No")
