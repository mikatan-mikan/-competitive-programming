N,P = map(int,input().split())

N *= 100
not_P = 100 - P
atk = 100
atk += P

cnt = 0

while True:
    cnt += 1
    N -= atk
    if N <= 0:
        print(cnt % 998244353)