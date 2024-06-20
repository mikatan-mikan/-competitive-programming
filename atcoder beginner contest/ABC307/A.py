n = int(input())

a = list(map(int, input().split()))

sum = 0

for i in range(1,n * 7 + 1):
    sum += a[i - 1]
    if i % 7 == 0:
        print(sum,end=" ")
        sum = 0