T = int(input())
def search():
    global leng,queue_1,queue_2
    while True:
            leng += 1
            tmp1 = [set(),set()]
            tmp2 = [set(),set()]
            for i,j in zip(queue_1[0],queue_2[1]):#まずはp1が赤からスタートする
                for ik in path[i]:
                    for jk in path[j]:
                        if C[ik - 1] != C[jk - 1]:
                            if ik == N:
                                print(leng)
                                return
                            tmp1[C[ik - 1]].add(ik)
                            tmp2[C[jk - 1]].add(jk)
            for i,j in zip(queue_1[1],queue_2[0]):
                for ik in path[i]:
                    for jk in path[j]:
                        if C[ik - 1] != C[jk - 1]:
                            if ik == N:
                                print(leng)
                                return
                            tmp1[C[ik - 1]].add(ik)
                            tmp2[C[jk - 1]].add(jk)
            queue_1[0] = tmp1[0]
            queue_1[1] = tmp1[1]
            queue_2[0] = tmp2[0]
            queue_2[1] = tmp2[1]
            if len(tmp1[0]) == 0 and len(tmp1[1]) == 0:
                print(-1)
                return

for i in range(T):
    N,M = map(int,input().split())
    path = [set() for _ in range(M + 1)]
    C = list(map(int,input().split()))
    for j in range(M):
        u,v = map(int,input().split())
        path[u].add(v)
        path[v].add(u)
    #bfsする
    queue_1 = [set(),set()]#赤,青
    queue_1[C[0]].add(1)
    queue_2 = [set(),set()]#赤,青
    queue_2[C[-1]].add(N)
    leng = 0
    search()

