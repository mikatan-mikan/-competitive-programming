
H,W = map(int,input().split())

C = list()
Ans_list = [0 for _ in range(W)]

for i in range(H):
    C.append(input())

for i in range(H):
    for j in range(W):
        if C[i][j] == "#":
            Ans_list[j] += 1


print(*Ans_list)
