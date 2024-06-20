n = int(input())

x = 0
y = 0

for i in range(n):
    a,b = map(int,input().split())
    x += a
    y += b

if x > y:
    print("Takahashi")
elif y > x:
    print("Aoki")
else:
    print("Draw")