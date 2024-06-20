n,m = map(int,input().split())

s = [input() for i in range(n)]

from collections import deque

visited = set()
que = deque()

x,y = 1,1
cnt = 0

def go(x,y,dx,dy):
    global cnt
    i = 0
    while True:
        i += 1
        if s[y + dy * i][x + dx * i] == ".":
            if s[y + (dy * (i + 1))][x + (dx * (i + 1))] == "#":
                if (y + dy * i, x + dx * i) not in visited:
                    if (y + dy * i, x + dx * i) not in visited :cnt += 1
                    visited.add((y + dy * i, x + dx * i))
                    que.append((y + dy * i, x + dx * i))
                    return
                else:
                    return
            if (y + dy * i, x + dx * i) not in visited :cnt += 1
            visited.add((y + dy * i, x + dx * i))
        else:
            return

visited.add((1,1))

while True:
    go(x,y,1,0)
    go(x,y,-1,0)
    go(x,y,0,1)
    go(x,y,0,-1)
    if len(que) == 0:
        break
    (y,x) = que.popleft()

# b : list[str] = s.copy()
# c = []

# for i in range(len(b)):
#     c.append(list(b[i]))


# for i in visited:
#     print(i)
#     c[i[0]][i[1]] = "o"

# print(*c,sep = "\n")

print(cnt + 1)