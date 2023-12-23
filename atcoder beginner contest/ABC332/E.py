n,d = map(int,input().split())

w = list(map(int,input().split()))

d_:list[list[int]] = [[0] for i in range(n)]

avg = 0

for i in w:
    avg += i / d
    #平均より最も低いd_を探す
    min_pl = 10000
    min_num = 10**9
    for j in range(len(d_)):
        if min_num > d_[j][-1]:
            min_pl = j
            min_num = d_[j][-1]
    d_[min_pl].append(0)
    d_[min_pl][-1] = d_[min_pl][-2] + i
