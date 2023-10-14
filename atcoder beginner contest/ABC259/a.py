N,M,X,T,D = map(int,input().split())

leng = 0

X_list = list(range(X))


leng += T#現在
leng -= X * D#0才
for i in X_list:
    if i == M:
        print(leng)
        exit()
    leng += D

print(leng)