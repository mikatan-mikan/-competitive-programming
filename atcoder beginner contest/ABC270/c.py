# 頂点数、始点、終点
N,X,Y = map(int,input().split())

path = list()
start_path = set()
end_path = set()

for i in range(N - 1):
    tmp = list(map(int,input().split()))
    if tmp[0] in start_path: 
    if tmp[1] in start_path:
    path.append(list(map(int,input().split())))


ans = list()
X = [X]

for i in range(N):
    for j in path:
        if j[0] in X:
            ans.append(j[0])
            X.append(j[1])
        if j[1] in X:
            ans.append(j[1])
            X.append(j[0])

print(*ans,X,path)
