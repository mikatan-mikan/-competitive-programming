N,K = map(int,input().split())
A = list(map(int,input().split()))
len_A = len(A)
end_flag = False
can_swap = N-K
for i in range(len_A):
    if len_A <= i+K:
        break
    if i <= can_swap:#並び替えれる範囲はN-Kまで
        if A[i] > A[i+K]:#並び替え先はi+K番目
            A[i],A[i+K] = A[i+K],A[i]
            for j in range(i+K,can_swap):
                if A[j] > A[i]:
                    A[j],A[i] = A[i],A[j]
b = sorted(A)
if b == A:
    print("Yes")
else:
    print("No")
