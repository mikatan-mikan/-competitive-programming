#```
#レベル毎に管理してみる

Blue_stone_list = [0,0,0,0,0,0,0,0,0,0,0]#lv 1 ~ 10を何個持っているか(分かりやすくするためlv0の分も確保)
Red_stone_list = [0,0,0,0,0,0,0,0,0,0,0]

N , X , Y = map(int,input().split())

Red_stone_list[N] += 1

while True:#変換できる石が無くなるまで繰り返す
    trade_red_flag = False#falseのまま=赤の石は現状交換できる在庫がない
    trade_blue_flag = False
    for i in range(2,11):#2から10番目の要素を探索(1lvは交換不可)
        if Red_stone_list[i] != 0:#そのレベルの石を持っているなら
            trade_red_flag = True#一回でも変更できたなら次も探索
            Red_stone_list[i - 1] += Red_stone_list[i]#赤い石のレベルは下がる
            Blue_stone_list[i] += (X * Red_stone_list[i])#同じレベルの青い石にX個変換
            Red_stone_list[i] = 0
        if Blue_stone_list[i] != 0:#同時に青い石も探索する
            trade_blue_flag = True
            Red_stone_list[i - 1] += Blue_stone_list[i]#レベルを落として赤い石に
            Blue_stone_list[i - 1] += (Y * Blue_stone_list[i])
            Blue_stone_list[i] = 0
    if trade_blue_flag == trade_red_flag and trade_blue_flag == False:
        break

print(Blue_stone_list[1])
#```