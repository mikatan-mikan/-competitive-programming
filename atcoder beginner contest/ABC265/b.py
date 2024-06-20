from collections import deque


N , M , T = map(int,input().split())

A = list(map(int,input().split()))


X = deque()
Y = deque()
for m in range(M):
    tmp1,tmp2 = map(int,input().split())
    X.append(tmp1)
    Y.append(tmp2)

bonus = 0
#10^5なので普通に前から進めてみる
for now_room in range(1,N):
    if T > A[now_room - 1]:
        T -= A[now_room - 1]
        try:
            if X[bonus] - 1 == now_room:
                T += Y[bonus]
                bonus += 1
        except:pass
    else:
        print("No")
        exit()
print("Yes")