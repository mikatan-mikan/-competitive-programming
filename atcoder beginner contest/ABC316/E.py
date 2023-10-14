import sys
sys.setrecursionlimit(10**9)


h,w = map(int,input().split())

field = [list(input()) for _ in range(h)]

break_conditions = set([">","<","v","^","#"])

def go_change(x,y,dx,dy):
    global field
    while True:
        x += dx
        y += dy
        if x < 0 or x >= w or y < 0 or y >= h:
            break
        else:
            if field[y][x] in break_conditions:
                return
            field[y][x] = "O"

start = (0,0)

#スタートを探す(ついでに通れない場所を#に置き換えておく)
for i in range(h):
    for j in range(w):
        if field[i][j] == "S":
            start = (i,j)
        elif field[i][j] == ">":
            go_change(j,i,1,0)
        elif field[i][j] == "<":
            go_change(j,i,-1,0)
        elif field[i][j] == "v":
            go_change(j,i,0,1)
        elif field[i][j] == "^":
            go_change(j,i,0,-1)


visited = set()
min_length = 10**9

def dfs(now,length):
    global min_length
    visited.add(now)
    for next in [(now[0]+1,now[1]),(now[0]-1,now[1]),(now[0],now[1]+1),(now[0],now[1]-1)]:
        if (next[0] < 0 or next[0] >= h or next[1] < 0 or next[1] >= w):
            continue
        if next not in visited:
            if field[next[0]][next[1]] == ".":
                dfs(next,length+1)
            elif field[next[0]][next[1]] == "G":
                min_length = min(min_length,length+1)

dfs(start,0)

print(min_length if min_length != 10**9 else -1)