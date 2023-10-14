n,h,w = map(int,input().split())

sy,sx = map(int,input().split())
#それぞれ-1
sy,sx = sy-1,sx-1

s = input()

c = [list(input().split()) for _ in range(h)]


for i in range(n):
    if s[i] == "F":
        sy -= 1
    elif s[i] == "B":
        sy += 1
    elif s[i] == "L":
        sx -= 1
    elif s[i] == "R":
        sx += 1
    print(c[sy][sx])
