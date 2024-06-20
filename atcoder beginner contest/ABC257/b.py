N,K,Q = map(int,input().split())

A_i = list(map(int,input().split()))
A_i = sorted(A_i)
L_i = list(map(int,input().split()))


for i in range(Q):
    if A_i[L_i[i] - 1] == N:
        continue
    elif A_i[L_i[i] - 1] + 1 not in A_i:#既に存在していなければ
        A_i[L_i[i] - 1] += 1

A_i = sorted(A_i)

print(*A_i)
