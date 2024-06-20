h,w = map(int,input().split())

a = [list(map(int,input().split())) for i in range(h)]

b = [list(map(int,input().split())) for i in range(h)]

cnt =0

def dfs(mode,i,a_):
    global cnt
    if mode == 0:
        a_[i],a_[i+1] = a_[i+1],a_[i]
    else:
        for j in range(w-1):
            a_[j][i],a_[j][i+1] = a_[j][i+1],a_[j][i]
    cnt += 1
    if a_ == b:
        print(cnt)
        exit()
    if cnt == h * w:
        return
    else:
        dfs(0,i+1,a_.copy())
        cnt -= 1
        dfs(1,i+1,a_.copy())
        cnt -= 1

for i in range(h - 1):
    dfs(0,i,a.copy())
for i in range(w - 1):
    dfs(1,i,a.copy())

print(-1)