n = int(input())

p = list(map(int,input().split()))

if p[0] == max(p):
    if max(p) not in p[1:]:
        print(0)
    else:
        print(1)
else:
    print(max(p[1:]) + 1 - p[0])