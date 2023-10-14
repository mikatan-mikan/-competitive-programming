from collections import deque

H,W = map(int,input().split())

S = deque()

flg = True
cnt = []
fir = 0

for i in range(H):
    S.append(input())

for i in range(H):
    cnt.append(0)
    for j in S[i]:
        if j == "#":
            if flg:
                fir = i
                flg = False
    if flg == False:# もし前回と#の数が違っていて、#が初めて見つかった行でなければ
        ck = 0
        for j in range(len(S[i]) + 1):
            if j != len(S[i]):
                if ck == 0 and S[i][j] == ".":
                    if i != 0:
                        if S[i - 1][j] == "#":
                            print(i + 1,j + 1)
                            exit()
                    if i != len(S[i]) - 1:
                        if S[i + 1][j] == "#":
                            print(i + 1,j + 1)
                            exit()
                elif ck == 0 and S[i][j] == "#":
                    ck = 1
                elif ck == 1 and S[i][j] == ".":
                    ck = 2
                    if i > 0:
                        if S[i - 1][j] == "#":
                            print(i + 1,j + 1)
                            exit()
                    elif i == 0:
                        if S[i + 1][j] == "#":
                            print(i + 1,j + 1)
                            exit()
                elif ck == 2 and S[i][j] == "#":
                    print(i + 1,j)
                    exit()
            elif i > 0:
                if ck == 2 and S[i - 1][j - 1] == "#":
                    print(i + 1,j)
                    exit()
            elif i == 0:
                if ck == 2 and S[i + 1][j - 1] == "#":
                    print(i + 1,j)
                    exit()
            
