n = int(input())

s = [input() for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if s[i] + s[j] == (s[i] + s[j])[::-1]:
            print("Yes")
            exit()

print("No")