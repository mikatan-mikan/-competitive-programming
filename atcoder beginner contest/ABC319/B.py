n = int(input())

s = ["-" for _ in range(n + 1)]

divi = []
#nの約数を求める
for i in range(1, 10):
    if n % i == 0:
        divi.append(i)


for i in range(n + 1):
    for j in divi:
        if i % (n/j) == 0:
            s[i] = j
            break

print(*s,sep="")