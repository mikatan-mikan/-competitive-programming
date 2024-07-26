sx,sy = map(int,input().split())

tx,ty = map(int,input().split())

if sx > tx:
    sx, tx = tx, sx
    sy, ty = ty, sy


x_diff = abs(tx - sx)

y_diff = abs(ty - sy)

if y_diff > x_diff:#縦移動を後からするパターン
    ans = x_diff + (y_diff - x_diff)
else:#横移動を後からするパターン
    ans = y_diff
    #斜め移動をした後yとxがどこかで式が変わる
    #移動後のyが偶数でxが奇数なら
    if ((sx + y_diff) % 2 == 1 and (sy + y_diff) % 2 == 0) or ((sx + y_diff) % 2 == 0 and (sy + y_diff) % 2 == 1):
        ans += (x_diff - y_diff + 1) // 2
    #移動後のyが奇数でxが偶数なら
    else:
        ans += (x_diff - y_diff) // 2

# ans = min(x_diff,y_diff) + abs(x_diff - y_diff)

print(ans)