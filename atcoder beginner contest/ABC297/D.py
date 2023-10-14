A,B = map(int,input().split())

cnt = 0

while True:
    if A == B:
        print(cnt)
        exit()
    elif A > B:
        tmp = A % B
        if tmp == 0:
            cnt += A // B - 1
            A = B
        else:
            cnt += A // B
            A = tmp
    else:
        tmp = B % A
        if tmp == 0:
            cnt += B // A - 1
            B = A
        else:
            cnt += B // A
            B = tmp