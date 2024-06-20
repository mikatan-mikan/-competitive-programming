import sys
sys.setrecursionlimit(10**9)

n,m = map(int,input().split())
s:list[str] | list[list] = [input() for _ in range(n)]

for i in range(n):
    s[i] = list(s[i])
    for j in range(m):
        if s[i][j] == "o":
            s[i][j] = True
        else:
            s[i][j] = False

ans = 10**9

#s[i] = 売り場
#s[i][j] = そこに味jが売っているか
def dfs(i,item,cnt):
    global ans
    for j in range(m):
        item[j] = item[j] or s[i][j]
    if False not in item:
        ans = min(ans,cnt)
        return
    if cnt >= ans:
        return
    for j in range(i + 1, n):
        dfs(j,item.copy(),cnt + 1)

for i in range(n):
    dfs(i,[False for _ in range(m)],1)

print(ans)