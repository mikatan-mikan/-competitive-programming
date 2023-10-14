x = input()
y = input()

c = len(x)
v = len(y)

if c > v :
    print("No")
    exit()

if x[0] == y[0] and x[c - 1] == y[c - 1]:
    print("Yes")
else:
    print("No")