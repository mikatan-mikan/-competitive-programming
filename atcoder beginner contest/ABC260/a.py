S = input()

for i in range(len(S)):
    count = 0
    for j in range(len(S)):
        if i == j:
            continue
        if S[j] == S[i]:
            break
        else:
            count += 1
    if count == 2:
        print(S[i])
        exit()

print(-1)