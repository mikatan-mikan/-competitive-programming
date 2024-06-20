n = int(input())
s = input()

import sys

sys.setrecursionlimit(10**9)

def rec(i,j):
    global ans
    if i == j:
        return 1
    tmp = rec(i,j + 1)
    ans += not (tmp and int(s[j]))
    ans += not (tmp and int(s[i]))
    return not (tmp and int(s[j]))

ans = 0

rec(n - 1,0)

print(ans)