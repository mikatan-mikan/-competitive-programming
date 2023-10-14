H,W = map(int,input().split())

S = [input() for _ in range(H)]

for i in range(H):
    for j in range(W - 1):
        if S[i][j] == "T" and S[i][j + 1] == "T":
            S[i] = S[i][:j] + "PC" + S[i][j + 2:]
print(*S,sep="\n")