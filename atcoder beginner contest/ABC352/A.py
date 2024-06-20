n,x,y,z = map(int,input().split())

if x > y:
    x,y = y,x

#yがおおきい
if y >= z >= x:
    print("Yes")
else:
    print("No")