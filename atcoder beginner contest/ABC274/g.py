from collections import deque


H,W = map(int,input().split())

S = deque()

for i in range(H):
    S.append(list(input()))
put = 0
for i in range(W):
    for j in range(H):
        if S[j][i] == "#" or S[j][i] == "N":
            continue
        length = 0#そこから見た最長
        tmp = 0
        for k in range(W - i):#右探索
            if S[j][i + k] == "#" or i + k == W - 1:
                if tmp > length:
                    if S[j][i + k] == ".":
                        tmp += 1
                    length = tmp
                    flag = 0
                break
            if S[j][i + k] == ".":
                tmp += 1
        tmp = 0
        for k in range(i):#左探索
            if S[j][i - k] == "#" or i - k == 0:
                if tmp > length:
                    if S[j][i - k] == ".":
                        tmp += 1
                    length = tmp
                    flag = 1
                break
            if S[j][i - k] == ".":
                tmp += 1
        tmp = 0
        for k in range(H - j):#下探索
            if S[j + k][i] == "#" or j + k == H - 1:
                if tmp > length:
                    if S[j + k][i] == ".":
                        tmp += 1
                    length = tmp
                    flag = 2
                break
            if S[j + k][i] == ".":
                tmp += 1
        tmp = 0
        for k in range(H - j):#上探索
            if S[j - k][i] == "#" or j - k == 0:
                if tmp > length:
                    if S[j - k][i] == ".":
                        tmp += 1
                    length = tmp
                    flag = 3
                break
            if S[j - k][i] == ".":
                tmp += 1
        tmp = 0
        if flag == 0:
            for k in range(length):
                S[j][i + k] = "N"
        if flag == 1:
            for k in range(length):
                S[j][i - k] = "N"
        if flag == 2:
            for k in range(length):
                S[j + k][i] = "N"
        if flag == 3:
            for k in range(length):
                S[j - k][i] = "N"
        put += 1

print(put)