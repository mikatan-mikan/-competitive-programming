N,K = map(int,input().split())

A = list(map(int,input().split()))

A.sort()
cnt = 0

def max_set(args):
    global mods
    max_stone = -1
    for j in A:
        if max_stone < j and j <= args:
            max_stone = j
            mods = args - j
    return max_stone

for i in range(N):
    max_stone = [[0,0]]
    for j in A:
        # 一番大きいAでかつ残りの石の数より小さいなら
        if j <= N:
            #余る数(5個って最後取れないより3個取って最後も3個取れる)*
            mod = N - j
            ##次々回加算分を算出して入れておく
            max_stone.append([j,j + max_set(mod - max_set(mod))])
    #もう石が取れないなら
    if max_stone == [[0]]:
        break
    ##次々回を見込んだうえで(ソート)
    max_stone.sort(key=lambda x:x[1])
    #高橋君のターンなら
    if i % 2 == 0:
        cnt += max_stone[-1][0]
    N -= max_stone[-1][0]

print(cnt)

