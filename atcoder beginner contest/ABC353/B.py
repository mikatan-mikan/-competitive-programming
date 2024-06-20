n,k = map(int,input().split())

a = list(map(int,input().split()))

start = 0
ptr = 0

while True:
    start += 1
    seat = k
    for i in range(ptr,len(a)):
        if seat >= a[i]:
            seat -= a[i]
            ptr = i + 1
        else:
            break

    if ptr == len(a):
        break

print(start)