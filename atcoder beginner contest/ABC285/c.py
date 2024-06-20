S = input()

v = 0

for i in range(len(S)):
    v += (ord(S[-(i + 1)]) - 64) * (26 ** i)
print(v)