N,M = map(int,input().split())
line = [sorted(list(map(int,input().split()))) for _ in range(M)]
line = sorted(line)#昇順でリスト構築

graph = [set([i + 1]) for i in range(N)]#くっついている辺を保存する

for i in range(M):
    for j in range(len(graph)):#現在保管しているリスト内にその辺が保管されているか
        if line[i][0] in graph[j]:#そのグループに含まれていたなら
            graph[j].add(line[i][1])#もう片方の辺を付け足す
        if line[i][1] in graph[j]:#同様に
            graph[j].add(line[i][0])


#最終的には1,2グループが結合できるなどの可能性があるので
pop_list = list()
for i in range(len(graph)):#全体の集合を見る
    now_set = list(graph[i])
    for j in range(len(graph[i])):#その結合内のものをみる
        for k in range(i + 1,len(graph)):#見る相手
            if now_set[j] in graph[k]:
                if k not in pop_list:
                    pop_list.append(k)

print(len(graph) - len(pop_list))