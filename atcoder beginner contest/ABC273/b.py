X , K = map(int,input().split())

# if len(str(X)) < K:
#     K = len(str(X))

for i in range(K):
    if X % (10 ** (i + 1)) >= 5 * (10 ** i):
        X = int(X / (10 ** (i + 1)))
        X = X * 10 ** (i + 1) + 10 ** (i + 1)
    else:
        X = int(X / (10 ** (i + 1)))
        X = X * 10 ** (i + 1)




print(X)