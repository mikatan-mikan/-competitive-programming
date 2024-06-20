N,K = map(int,input().split())
A = list(map(int,input().split()))
end_flag = False
can_swap = N-K
for i in range(len(A)):
    if A[i] <= can_swap:
        try:
            if A[i] < A[i+K]:
                A[i] = A[i+K]
        except:
            pass
    else:
        try:
            if A[i+2] < A[i]:
                print("No")
                end_flag = True
        except:
            try:
                if A[i+1] < A[i]:
                    print("No")
                    end_flag = True
            except:pass
    if end_flag:
        exit()
print("Yes")
