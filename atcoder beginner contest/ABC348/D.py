#再帰上限の設定
import sys
sys.setrecursionlimit(10**9)

h,w = map(int,input().split())

a = [list(input()) for _ in range(h)]

n = int(input())

start = (0,0)

next_ = [(1,0),(-1,0),(0,-1),(0,1)]

a.insert(0,['#'] * (w + 2))
for i in range(1,h + 1):
    a[i].insert(0,'#')
    a[i].append('#')
    for j in range(1,w + 1):
        if a[i][j] == 'S':
            start = (i,j)
a.append(['#'] * (w + 2))

for i in range(n):
    r,c,e = map(int,input().split())
    if a[r][c] != 'T':
        a[r][c] = str(e)

normal = set(['#','.','T','S'])

#枝狩りをする(その場所にそのエネルギー量より低い状態で来ていたらどうせたどり着けないという指標)
a_energy = [[-1 for _ in range(w + 1)] for _ in range(h + 1)]

def dfs(y,x,hp,visited,energy_visited):
    #エネルギーが前回きた時より低いなら
    if a_energy[y][x] >= hp:
        return
    a_energy[y][x] = hp
    #a[y][x]がintなら
    if a[y][x] not in normal and y + x * 300 not in energy_visited:
        if int(a[y][x]) > hp:
            hp = int(a[y][x])
            visited.clear()
        energy_visited.add(y + x * 300)
    if a[y][x] == 'T':
        print("Yes")
        exit()
    if hp == 0:
        return
    visited.add(y + x * 300)
    for mv in next_:
        if (y + mv[0]) + (x + mv[1]) * 300 not in visited:
            if a[y + mv[0]][x + mv[1]] != '#':
                dfs(y + mv[0],x + mv[1],hp - 1,visited,energy_visited)
    if y + x * 300 in visited:
        visited.remove(y + x * 300)
        


dfs(start[0],start[1],0,set(),set())
print("No")