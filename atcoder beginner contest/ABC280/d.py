K = int(input())

N = 1

ext = 1

while True:
    N *= ext
    if N % K == 0:
        print(ext)
        exit()
    ext += 1