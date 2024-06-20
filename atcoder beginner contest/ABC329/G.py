n,q = map(int,input().split())

c = list(map(int,input().split()))

case_ = [set([c[i]]) for i in range(n)]

for i in range(q):
    query = list(map(int,input().split()))
    #aをbに移す
    #要素が大きいならswapしてしまう
    if len(case_[query[0] - 1]) > len(case_[query[1] - 1]):
        case_[query[0] - 1], case_[query[1] - 1] = case_[query[1] - 1], case_[query[0] - 1]
        for j in case_[query[0] - 1]: case_[query[1] - 1].add(j)
        case_[query[0] - 1].clear()
        print(len(case_[query[1] - 1]))
    else:
        for j in case_[query[0] - 1]: case_[query[1] - 1].add(j)
        case_[query[0] - 1].clear()
        print(len(case_[query[1] - 1]))