N,Q = map(int,input().split())
A = list(map(int,input().split()))
D = [0,0,0]
for i in range(Q):
    query = input().split()
    if query[0] == '1':
        A[int(query[1]) - 1] = int(query[2])
        print("A",A)
    elif query[0] == '2':
        D[0] = A[0]
        D[1] += i for i in range(N)
        D[2] = ((A[0] + A[1] + A[2]) + A[0] + A[1] + A[0]) + (A[0] + (A[0] + A[0] + A[1]))
        print(D[int(query[1]) - 1])