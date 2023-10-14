
K = int(input())

if K >= 60:
    a = 1
    K -= 60
else:
    a = 0

a = 21 + a
b = ":"
if K <= 9:
    b = ":0"

print(str(a) + str(b) + str(K))