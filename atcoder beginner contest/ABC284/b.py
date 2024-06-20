T = int(input())

for i in range(T):
    N = int(input())
    A = list(map(int,input().split()))
    cnt = 0
    for i in range(N):
        if A[i] % 2 == 1:
            cnt += 1
    print(cnt)