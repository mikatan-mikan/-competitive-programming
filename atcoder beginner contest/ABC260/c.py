#```py
from collections import deque


Blue_stone_list = deque()
Red_stone_list = deque()

Red_stone_list.append(0)

Red_stone_list[0] , X , Y = map(int,input().split())

rande_x = range(X)
range_y = range(Y)

while True:#変換できる石が無くなるまで繰り返す
    trade_red_flag = False#falseのまま=赤の石は現状交換できる在庫がない
    trade_blue_flag = False
    for i in range(len(Red_stone_list)):#赤の石の中を見る
        if Red_stone_list[i] >= 2:#赤い石のレベルが2以上なら
            trade_red_flag = True
            for _ in rande_x:#レベル n の青い宝石 X 個を受け取る
                Blue_stone_list.append(Red_stone_list[i])
            Red_stone_list[i] -= 1#レベル n−1 の赤い宝石 1 個と交換=持っている石のレベルが下がる
    for i in range(len(Blue_stone_list)):#青い石の中を見る
        if Blue_stone_list[i] >= 2:#青の石のレベルが2以上なら
            trade_blue_flag = True
            for _ in range_y:#レベル n−1 の青い宝石 Y 個を受け取る
                Blue_stone_list.append(Blue_stone_list[i] - 1)
            Red_stone_list.append(Blue_stone_list[i] - 1)#レベル n−1 の赤い宝石 1 個を交換
            Blue_stone_list.remove(Blue_stone_list[i])#交換するので当然消える
    if trade_blue_flag == trade_red_flag and trade_blue_flag == False:
        break

print(len(Blue_stone_list))

#```