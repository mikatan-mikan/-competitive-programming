##後ろのmin(10,n)文字の中に違う文字が含まれていたならNo

N,K = map(int,input().split())

A = list(map(int,input().split()))

Q = int(input())

place = [list(map(int,input().split())) for _ in range(Q)]

K = min(10,N)

use = set()

for i in range(Q):
    flg = False
    now_str = A[place[i][0] - 1:place[i][1]]
    for j in range(1,len(now_str) - K + 1 + 1):
        if now_str[-j] not in use:
            use.add(now_str[-j])
        else:
            print("No")
            flg = True
            break
    if flg:continue
    print("Yes")