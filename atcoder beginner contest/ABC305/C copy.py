from collections import deque

H,W = map(int,input().split())

S = deque()

flg = True
cnt = []
fir = 0

for i in range(H):
    S.append(input())

for i in range(H):
    for j in range(W):
        cnt = 0
        if S[i][j] == ".":
            if i > 1:
                if S[i - 1][j] == "#":
                    cnt += 1
            if i < H - 1:
                if S[i + 1][j] == "#":
                    cnt += 1
            if j > 0:
                if S[i][j - 1] == "#":
                    cnt += 1
            if j < W - 1:
                if S[i][j + 1] == "#":
                    cnt += 1
        if cnt >= 2:
            print(i + 1,j + 1)
            exit()