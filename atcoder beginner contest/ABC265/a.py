X , Y ,  N  = map(int,input().split())

if 3 * X <= Y :#3つ同時の方が高いなら
    print(N * X)

else:
    print(Y * int(N / 3) + X * (N % 3))

