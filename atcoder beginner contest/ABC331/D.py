n, q = map(int, input().split())

# グリッドの各行を受け取る
field = [input() for _ in range(n)]

# 二次元累積和を計算する前処理
prefix_sum = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(n):
    for j in range(n):
        color = 1 if field[i][j] == 'B' else 0
        prefix_sum[i + 1][j + 1] = prefix_sum[i][j + 1] + prefix_sum[i + 1][j] - prefix_sum[i][j] + color

for i in range(q):
    ans = 0
    y1, x1, y2, x2 = map(int, input().split())
    # きれいな盤面を先に計算
    x_1 = x1 // n
    x1 -= x_1 * n
    x2 -= x_1 * n
    y_1 = y1 // n
    y1 -= y_1 * n
    y2 -= y_1 * n
    x = (x2 - n) // n
    y = (y2 - n) // n
    ans += prefix_sum[-1][-1] * (x*y)
    #左上
    #余った切れ端部分を求める
    #0,0が始点の場合
    if x1 == 0 and y1 == 0:
        ans += prefix_sum[y2][x2] - prefix_sum[y1][x2] - prefix_sum[y2][x1] + prefix_sum[y1][x1]
    #x2がnを超えていてy2もnを超えている場合
    if x2 >= n - 1 and y2 >= n:
        ans += prefix_sum[-1][-1] - prefix_sum[y1][-1] - prefix_sum[-1][x1] + prefix_sum[y1][x1]
    #y2がnを超えずx2はnを超えている場合
    elif x2 >= n:
        ans += prefix_sum[y2][-1] - prefix_sum[y1][-1] - prefix_sum[y2][x1] + prefix_sum[y1][x1]
    #y2がnを超えていてx2がnを超えない場合
    elif y2 >= n:
        ans += prefix_sum[-1][x2] - prefix_sum[-1][x1] - prefix_sum[y2][x1] + prefix_sum[y1][x1]
    #x2もy2もnを超えていない場合
    else:
        ans += prefix_sum[y2][x2] - prefix_sum[y1][x2] - prefix_sum[y2][x1] + prefix_sum[y1][x1]
    print(ans)