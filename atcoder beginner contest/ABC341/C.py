h,w,n = map(int,input().split())

t = input()

s = [input() for _ in range(h)]

ans = 0

for i in range(h):
    for j in range(w):
        if s[i][j] == "#":
            continue
        now = [i,j]
        is_goal = True
        for move in t:
            if move == "U":
                now[0] -= 1
            elif move == "D":
                now[0] += 1
            elif move == "L":
                now[1] -= 1
            elif move == "R":
                now[1] += 1
            if s[now[0]][now[1]] == "#":
                is_goal = False
                break
        if is_goal:
            ans += 1

print(ans)