from collections import deque


S = [input() for _ in range(9)]

place = set()

# 一点を取って他のすべての点までの距離を見る
# その距離と等しい点を順に見つけれたなら正方形である
# その正方形のデータを二次元タプルでsetに保存
# 次回以降重複してなければカウント

# 4点があるかを判定する
# ただし、右方向しか見ない(左方向は以前の探索or今後発見される)
# つまり一点目->二点目が左上、左下であるとき正しい答えを返す
def re_check(p2p,point_1,point_2):
    global place
    #以下の二点が存在すれば正方形
    #座標軸を90度回転させる
    p2p_90 = [-p2p[1],p2p[0]]
    #座標軸を180度回転させる
    p2p_180 = [-p2p_90[1],p2p_90[0]]
    try:
        if point_2[0] + p2p_90[0] < 0 or point_2[1] + p2p_90[1] < 0 or point_2[0] + p2p_90[0] + p2p_180[0] < 0 or point_2[1] + p2p_90[1] + p2p_180[1] < 0:
            return
        if S[point_2[0] + p2p_90[0]][point_2[1] + p2p_90[1]] == "#" and S[point_2[0] + p2p_90[0] + p2p_180[0]][point_2[1] + p2p_90[1] + p2p_180[1]] == "#":
            place.add(tuple(sorted([tuple(point_1),tuple(point_2),tuple([point_2[0] + p2p_90[0],point_2[1] + p2p_90[1]]),tuple([point_2[0] + p2p_90[0] + p2p_180[0],point_2[1] + p2p_90[1] + p2p_180[1]])])))
    except:# その点の場所が存在しないなら
        pass


sharp_place = deque()

for i in range(9):
    for j in range(9):
        if S[i][j] == "#":
            sharp_place.append(deque([i,j]))

for i in sharp_place:#ある点から
    for j in sharp_place:#ある点に向かって
        if i == j:#同じ点を指しているなら
            continue
        len_p2p = [j[0] - i[0],j[1] - i[1]]#[y座標の差,x座標の差]
        # if len_p2p[0] < 0 or len_p2p[1] < 0:#既に探索済みであるため
        #     continue
        re_check(len_p2p,i,j)

print(len(place))
