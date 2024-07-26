n,t = map(int,input().split())

s = input()

x = list(map(int,input().split()))

x_s = sorted(zip(x, s), key=lambda ant: ant[0])

x, s = list(zip(*x_s))

first = None
#始めの一匹目を探す
for i in range(n):
    if s[i] == "1":
        first = i
        break

if first == None:#全員同じ方向(-方向)
    print(0)
    exit()

from collections import deque

ans = 0
area_cnt = deque([x[first]])#虫が現在の先端から遡ってt前にいるかどうか
for i in range(first + 1,n):
    #現在地点から遡っていない虫を排除
    while True:
        if len(area_cnt) == 0:
            break
        if abs(x[i] - area_cnt[0]) > t * 2:#t(お互いにtずつ動いた時)の距離を超えたら
            area_cnt.popleft()
        else:
            break
    #+方向だけ意識すればよい(-とぶつかるか検証すればよい)
    if s[i] == "1":
        area_cnt.append(x[i])
    else:#ぶつかるなら
        ans += len(area_cnt)

print(ans)