
import sys
sys.setrecursionlimit(10 ** 9)


N,M = map(int,input().split())

path = [list() for _ in range(N + 1)]

for i in range(M):
    u,v = map(int,input().split())
    path[u].append(v)
    path[v].append(u)

re = set()

def dfs(place):
    global re
    #もしplaceが既に行ったことがあるなら
    if place in re:
        print("No")
        exit()
    re.add(place)
    #分岐があったなら(来た道 + 行く道が2以上なら)
    if len(path[place]) > 2:
        print("No")
        exit()
    #次の場所に進む
    for next in path[place]:
        if next not in re:
            dfs(next)

zero = 0
for i in range(1,N + 1):
    if len(path[i]) == 0:
        print("No")
        exit()
    elif len(path[i]) == 1:
        ##ここから深さ優先して、全ての1-Nを通ればYes
        dfs(i)
        for j in range(1,N + 1):
            if j in re:#行ったことあるなら
                continue
            else:#一回も行ったことがないなら
                print("No")
                exit()
        #最後までの全てが行ったことがあるなら
        print("Yes")
        exit()
    elif len(path[i]) == 2:
        continue
    else:
        print("No")
        exit()

print("Yes")


# re = set()
# loop = True

# def dfs(place,bef):
#     global re
#     re.add(place)
#     #分岐があったなら(来た道 + 行く道が2異常なら)
#     if len(path[place]) > 2:
#         print("No")
#         exit()
#     #次の場所に進む
#     for next in path[place]:
#         if bef not in re:
#             dfs(next,place)

# flg = 0

# for i in range(1,N + 1):
#     if len(path[i]) == 1 and flg == 0:
#         loop = False
#         dfs(i,None)
#         flg += 1
#     elif len(path[i]) == 1 and flg == 1:
#         flg += 1
#     elif len(path[i]) > 2 or len(path[i]) == 0:
#         print("No")
#         exit()
#     elif flg == 2:
#         print("No")
#         exit()

# if loop:
#     print("No")
# else:
#     print("Yes")