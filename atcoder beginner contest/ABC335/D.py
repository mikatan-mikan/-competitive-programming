n = int(input())

l: list[list[int|str]] = [[0 for _ in range(n + 2)] for _ in range(n + 2)]

for i in range(n + 2):
    l[i][0] = -1
    l[i][-1] = -1
    l[0][i] = -1
    l[-1][i] = -1

l[(n + 1)//2][(n + 1) // 2] = "T"

now = [1,1]
n_n = 1

now_dir = "R"

while True:
    l[now[1]][now[0]] = n_n
    n_n += 1
    if n_n == n ** 2:
        break
    if now_dir == "D":
        if l[now[1] + 1][now[0]] != 0:
            now_dir = "L"
            now[0] -= 1
            continue
        now[1] += 1
    elif now_dir == "U":
        if l[now[1] - 1][now[0]] != 0:
            now_dir = "R"
            now[0] += 1
            continue
        now[1] -= 1
    elif now_dir == "R":
        if l[now[1]][now[0] + 1] != 0:
            now_dir = "D"
            now[1] += 1
            continue
        now[0] += 1
    elif now_dir == "L":
        if l[now[1]][now[0] - 1] != 0:
            now_dir = "U"
            now[1] -= 1
            continue
        now[0] -= 1

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(l[i][j], end=" ")
    print()