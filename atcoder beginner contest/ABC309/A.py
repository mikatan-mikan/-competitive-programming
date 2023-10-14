a,b = map(int,input().split())

if a + 1 == b:
    if b != 4 and b != 7:
        print("Yes")
        exit()

print("No")