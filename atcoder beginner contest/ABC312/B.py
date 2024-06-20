n,m = map(int,input().split())

s = [input() for _ in range(n)]

from collections import deque

ans = deque()

for i in range(n - 8):
    for j in range(m - 8):
        if (i == 0 and j == 9) : 
            pass
        #3*3の領域が#
        if s[i][j] == "#" and s[i + 1][j] == "#" and s[i + 2][j] == "#" and s[i][j + 1] == "#" and s[i + 1][j + 1] == "#" and s[i + 2][j + 1] == "#" and s[i][j + 2] == "#"  and s[i + 1][j + 2] == "#" and s[i + 2][j + 2] == "#":
            #3*3の領域が#
            k,l = i + 6, j + 6
            if s[k][l] == "#" and s[k + 1][l] == "#" and s[k + 2][l] == "#" and s[k][l + 1] == "#" and s[k + 1][l + 1] == "#" and s[k + 2][l + 1] == "#" and s[k][l + 2] == "#"  and s[k + 1][l + 2] == "#" and s[k + 2][l + 2] == "#":
                #その周りが.
                if s[i + 3][j] == "." and s[i + 3][j + 1] == "." and s[i + 3][j + 2] == "." and s[i + 3][j + 3] == "." and s[i][j + 3] == "." and s[i + 1][j + 3] == "." and s[i + 2][j + 3] == ".":
                    #klに対してその周り
                    if s[k - 1][l - 1] == "." and s[k - 1][l] == "." and s[k - 1][l + 1] == "." and s[k - 1][l + 2] == "." and s[k][l - 1] == "." and s[k + 1][l - 1] == "." and s[k + 2][l - 1] == ".":
                        ans.append((i + 1,j + 1))

for i in ans:
    print(*i)