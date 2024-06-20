N = int(input())


H = list(map(int,input().split()))

max = 0
num = 0
for i in range(N):
    if max < H[i]:
        max = H[i]
        num = i + 1

print(num)