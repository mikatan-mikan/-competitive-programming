A = list(map(int,input().split()))

s = 0

for i in range(len(A)):
    if A[i] == 0:
        continue
    else:
        s += (2 ** (i))

print(s)