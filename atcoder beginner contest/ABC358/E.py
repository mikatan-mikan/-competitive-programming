h,w,k = map(int,input().split())

move = [[0,""] for _ in range(h + 1)]#それぞれの高さについて何回移動するか

## 横移動は戻る挙動がいるので2n回の移動
## 縦移動はその挙動以外なのでh - 2n回で奇数偶数が反転しない(kが奇数ならhは奇数出ないといけない)

if h > k:#高さが要求される歩数より多い場合
    print(-1)
    exit()
if k % 2 != h % 2:#kとhの偶奇が異なる場合
    print(-1)
    exit()


need_move = k - h#必然的に移動する数を引いた数が必須の移動数
if need_move > 0:
    for i in range(0,h,2):
        move[i][0] = min(need_move // 2,w - 1)
        move[i][1] = "GO"
        move[i + 1][1] = "RETURN"
        need_move -= move[i][0] * 2
        if need_move <= 0:
            break

#この時点で高さが奇数ならneed_moveが最大一列分残る

field = [["" for _ in range(w * 2 + 1)] for _ in range(h * 2 + 1)]
for i in range(w * 2 + 1):
    field[0][i] = "+"
    field[-1][i] = "+"
field[0][-2] = "S"
field[-1][-2] = "G"

for i in range(h):
    for j in range(w):
        field[i*2 + 1][j*2 + 1] = "o"
        field[i*2 + 1][j*2] = "."
    field[i*2 + 1][0] = "+"
    field[i*2 + 1][-1] = "+"
    if move[i][1] == "":
        field[i*2][0] = "+"
        for j in range(w - 1):
            field[i*2][j*2 + 1] = "-"
            field[i*2][j*2] = "+"
        field[i*2][-3] = "+"
        field[i*2][-2] = "."
        field[i*2][-1] = "+"
    elif move[i][1] == "GO":
        for j in range(w - 1,move[i][0],-1):
            field[i*2 + 2][j*2 + 1] = "-"
            field[i*2 + 2][j*2] = "+"
        field[i*2 + 2][j*2 + 1] = "."
    else:
        for j in range(move[i][0]):
            field[i*2 + 1][j*2 + 1] = "."


print(*field,sep = "\n")
