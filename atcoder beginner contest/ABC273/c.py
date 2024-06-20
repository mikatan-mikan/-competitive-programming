N = int(input())

A = set(map(int,input().split()))

now_num = N
cnt = 0

for i in range(N): #0からn-1(K)まで:
    if i in A:
        A.remove(i)
    print(len(A))