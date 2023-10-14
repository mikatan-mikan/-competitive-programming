S = input()

num = -1

for i in range(len(S)):
    if S[i] == "a":
        num = i + 1

print(num)