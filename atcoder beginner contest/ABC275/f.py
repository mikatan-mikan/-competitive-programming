from collections import deque


N,M = map(int,input().split())
a = deque(map(int,input().split()))

for x in range(M):#1..M
    num_set = a.copy()
    for j in range(N):#aの全要素
        #最初にxを超える数を削除する
        if a[j] > x:
            num_set.remove(a[j])
        #次に1から順に