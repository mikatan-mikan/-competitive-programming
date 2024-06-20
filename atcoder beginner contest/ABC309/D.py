
n1,n2,m = map(int,input().split())

path = [list() for _ in range(n1 + n2 + 1)]

for i in range(m):
    a,b = map(int,input().split())
    path[a].append(b)
    path[b].append(a)

visited = set([1])
max_len = [0,0]

now = 0
que = list()
que_read = 0
que.append([path[1],0])
leng = [0 for _ in range(n1 + n2 + 1)]

while que:# bfs
    for i in que:
        max_len[0] = i[1]
        for j in i[0]:
            if j not in visited:
                visited.add(j)
                que.append([path[j], i[1] + 1])
    del que[0]

visited = set([n1 + n2])
now = 0
que = list()
que_read = 0
que.append([path[n1 + n2],0])
leng = [0 for _ in range(n1 + n2 + 1)]

while que:# bfs
    for i in que[que_read:]:
        max_len[1] = i[1]
        for j in i[0]:
            if j not in visited:
                visited.add(j)
                que.append([path[j], i[1] + 1])
    del que[0]



print(sum(max_len) + 1)