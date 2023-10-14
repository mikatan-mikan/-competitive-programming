n,m = map(int,input().split())



from collections import deque

path = deque([[] for _ in range(n + 1)])#i番目の人よりpath[i]番目の方が強い
path_weak = deque([[] for _ in range(n + 1)])

for i in range(m):
    a,b = map(int,input().split())
    path[b].append(a)#b番目よりa番目の方が強い
    path_weak[a].append(b)#a番目よりb番目の方が強い

flg = False
pl = None

for i in range(len(path)):
    if i == 0:
        continue
    if path[i] == []:
        if flg:
            print(-1)
            exit()
        pl = i
        flg = True

print(pl)