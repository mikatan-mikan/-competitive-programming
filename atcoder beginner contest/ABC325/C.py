import sys

sys.setrecursionlimit(10**9)

gh,gw = map(int,input().split())

s = [input() for _ in range(gh)]

visited = set()
cnt = 0

def dfs(w,h):
    visited.add((w,h))
    for next in [(w+1,h),(w-1,h),(w,h+1),(w,h-1),(w+1,h+1),(w+1,h-1),(w-1,h+1),(w-1,h-1)]:
        if next[1] < 0 or next[1] >= gh or next[0] < 0 or next[0] >= gw:
            continue
        if next not in visited and s[next[1]][next[0]] == "#":
                dfs(next[0],next[1])

for i in range(gw * gh):
    if (i%gw,i//gw) not in visited and s[i // gw][i % gw] == "#":
        cnt += 1
        dfs(i%gw,i//gw)

print(cnt)