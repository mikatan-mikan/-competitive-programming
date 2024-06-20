from collections import deque
H,W = map(int,input().split())

C = deque()
flag_map = [[0 for _ in range(W)] for __ in range(W)]

for i in range(H):
    C.append(input())
break_flag = False
start = [0,0]
for i in range(H):
    for j in range(W):
        if C[i][j] == "S":
            start = [i,j]
            break_flag = True
            break
    if break_flag:break

flag_map[start[0]][start[1]] = 2
move = [(0,1),(0,-1),(1,0),(-1,0)]

que = deque([start])
cnt = 0
while que:
    cnt += 1
    now = que.popleft()
    for d in move:
        if now[0] + d[0] < 0 or now[1] + d[1] < 0 or now[0] + d[0] >= W or now[1] + d[1] >= H: continue
        if C[now[0] + d[0]][now[1] + d[1]] and flag_map[now[0] + d[0]][now[1] + d[1]] == 0:
            flag_map[now[0] + d[0]][now[1] + d[1]] = 1
            que.append([now[0] + d[0],now[1] + d[1]])
        elif C[now[0] + d[0]][now[1] + d[1]] and flag_map[now[0] + d[0]][now[1] + d[1]] == 2 and cnt > 5:
            print("Yes")
            exit()

print("No")