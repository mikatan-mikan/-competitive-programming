from collections import deque


H , W = map(int,input().split())

G = list()
for gin in range(H):
    G.append(input())

place = [0,0]
place_his = deque([[0,0]])

def else_place(now_place):
    print(now_place[0] + 1,now_place[1] + 1)
    exit()

#とりあえず元に戻れば無限ループするので[\
i = 0
while True:
    i += 1
    now_place_char = G[place[0]][place[1]]
    if now_place_char == "U":
        if place[0] != 0:
            place[0] -= 1
        else:
            else_place(place)
    elif now_place_char == "D":
        if place[0] != H - 1:
            place[0] += 1
        else:
            else_place(place)
    elif now_place_char == "L":
        if place[1] != 0:
            place[1] -= 1
        else:
            else_place(place)
    else:
        if place[1] != W - 1:
            place[1] += 1
        else:
            else_place(place)
    if i % 1000 == 0:
        if place in place_his:
            print(-1)
            exit()
    place_his.append(place.copy())