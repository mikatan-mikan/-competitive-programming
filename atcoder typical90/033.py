h,w = map(int,input().split())

if (h == 1 or w == 1):
    print(h * w)
    exit()

h = (h + 1) // 2
w = (w + 1) // 2

print(h * w)