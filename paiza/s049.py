n,x,f,s = map(int,input().split())

min_ = float("inf")

import sys
sys.setrecursionlimit(10**9)

def dfs(time,conditions,write_code,now_code = 0):
    global min_
    if conditions[0] == "no_sleep":
        if write_code > 0:#寝ないなら
            if now_code + write_code >= n:
                if time < min_:
                    min_ = time + 1
                return
            dfs(time + 1,conditions,write_code - f,now_code + write_code)
        if write_code != x:#寝るなら
            dfs(time + 3,["no_sleep",0],write_code + s if write_code + s <= x else x,now_code)

dfs(0,["no_sleep",0],x)

print(min_)