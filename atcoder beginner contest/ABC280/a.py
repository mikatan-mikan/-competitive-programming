H,W = map(int,input().split())

S = []

for i in range(H):
    S.append(input())

cnt = 0

for i in range(W):
    for j in range(H):
        if S[j][i] == "#":
            cnt += 1

print(cnt)