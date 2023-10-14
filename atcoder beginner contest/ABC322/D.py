
#ミノ
p_in = [[list(input()) for _ in range(4)] for _ in range(3)]
p = [[[[".",".",".","."] for _ in range(4)] for _ in range(3)] for _ in range(4)]
p[0] = p_in
#p[1]からp[3]に回転後のミノのデータを詰める
for rot in range(1,4):
    for mino in range(3):
        for x in range(4):
            for y in range(4):
                p[rot][mino][y][x] = p[rot - 1][mino][3 - x][y]

#左端or上に何もなければ図形を詰める
for rot in range(0,4):
    for mino in range(3):
        #上に何もなければ
        if p[rot][mino][0] == [".",".",".","."]:
            del p[rot][mino][0]
            p[rot][mino].append([".",".",".","."])
            if p[rot][mino][0] == [".",".",".","."]:
                del p[rot][mino][0]
                p[rot][mino].append([".",".",".","."])
                if p[rot][mino][0] == [".",".",".","."]:
                    del p[rot][mino][0]
                    p[rot][mino].append([".",".",".","."])
        #左に何もなければ
        for x in range(4):
            if p[rot][mino][0][0] == "." and p[rot][mino][1][0] == "." and p[rot][mino][2][0] == "." and p[rot][mino][3][0] == ".":
                del p[rot][mino][0][0]
                p[rot][mino][0].append(".")
                del p[rot][mino][1][0]
                p[rot][mino][1].append(".")
                del p[rot][mino][2][0]
                p[rot][mino][2].append(".")

# for i in range(4):
#     for j in range(3):
#         print(*p[i][j],sep = "\n")
#         print()




field = [["" for _ in range(7)] for _ in range(7)]

# 3つのミノをrotと座標を変えながら実際に設置する

for rot_mino1 in range(4):
    for rot_mino2 in range(4):
        for rot_mino3 in range(4):
        #     if rot_mino1 == 1 and rot_mino2 == 0 and rot_mino3 == 1:
        #         pass
        #         dat_1 = p[rot_mino1][0]
        #         dat_2 = p[rot_mino2][1]
        #         dat_3 = p[rot_mino3][2]
            for base_x_1 in range(4):
                for base_y_1 in range(4):
                    for base_x_2 in range(4):
                        for base_y_2 in range(4):
                            for base_x_3 in range(4):
                                for base_y_3 in range(4):
                                    if base_x_1 == 0 and base_y_1 == 0 and base_x_2 == 0 and base_y_2 == 1 and base_x_3 == 0 and base_y_3 == 0 and rot_mino1 == 0 and rot_mino2 == 2 and rot_mino3 == 0:
                                         pass
                                    field = [["" for _ in range(7)] for _ in range(7)]
                                    isComp = True
                                    for x in range(4):
                                        for y in range(4):
                                            #もしfield[y][x]がすでに#で#を書き込もうとしているならfail
                                            if (field[base_y_1 + y][base_x_1 + x] == "#" and p[rot_mino1][0][y][x] == "#") or (field[base_y_2 + y][base_x_2 + x] == "#" and p[rot_mino2][1][y][x] == "#") or (field[base_y_3 + y][base_x_3 + x] == "#" and p[rot_mino3][2][y][x] == "#"):
                                                isComp = False
                                                break
                                            #もしyかxが4以上で#を書き込もうとしているならfail
                                            if (y >= 4 or x >= 4) and (p[rot_mino1][0][y][x] == "#" or p[rot_mino2][1][y][x] == "#" or p[rot_mino3][2][y][x] == "#"):
                                                isComp = False
                                                break
                                            field[base_y_1 + y][base_x_1 + x] = "#" if p[rot_mino1][0][y][x] == "#" else field[base_y_1 + y][base_x_1 + x]
                                            field[base_y_2 + y][base_x_2 + x] = "#" if p[rot_mino2][1][y][x] == "#" else field[base_y_2 + y][base_x_2 + x]
                                            field[base_y_3 + y][base_x_3 + x] = "#" if p[rot_mino3][2][y][x] == "#" else field[base_y_3 + y][base_x_3 + x]
                                        if not isComp:
                                            break
                                    if isComp:
                                        #4*4が埋まっているか
                                        isMiss = False
                                        for ck in range(4):
                                            if field[ck][0] != "#" or field[ck][1] != "#" or field[ck][2] != "#" or field[ck][3] != "#":
                                                isMiss = True
                                                break
                                        if isMiss:
                                            continue
                                        # print(base_x_1,base_y_1,base_x_2,base_y_2,base_x_3,base_y_3,rot_mino1,rot_mino2,rot_mino3)
                                        print("Yes")
                                        exit()


print("No")