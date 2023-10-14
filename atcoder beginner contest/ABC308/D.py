from collections import deque

h,w = map(int,input().split())

s = []
next = dict({"s":"n","n":"u","u":"k","k":"e","e":"s"})
visited = set()


for i in range(h):
    s.append(input())

que = deque([(0,0)])

if s[0][0] == "s":
    while que:
        x, y = map(int,que.pop())
        visited.add((x,y))
        if x == w-1 and y == h-1:
            print("Yes")
            exit()
        for dx, dy in [(1,0),(0,1),(-1,0),(0,-1)]:
            if 0 <= x+dx < w and 0 <= y+dy < h:
                if s[y + dy][x + dx] == next[s[y][x]] and (x+dx,y+dy) not in visited:
                    que.append((x+dx, y+dy))


print("No")