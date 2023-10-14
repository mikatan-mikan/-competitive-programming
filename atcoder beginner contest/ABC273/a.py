N = int(input())

def re(k):
    if k == 0:return 1
    return k * re(k - 1)

if N==0:
    print(1)
else:
    print(re(N))
