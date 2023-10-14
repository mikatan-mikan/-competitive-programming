N = int(input())
A_i = []
for i in range(N):
    A_i.append([])
    for j in range(i + 1):
        if j == 0:
            A_i[i].append(1)
        elif j == i:
            A_i[i].append(1)
        else:
            A_i[i].append(A_i[i-1][j-1] + A_i[i-1][j])

for i in range(len(A_i)):
    print(*A_i[i])

