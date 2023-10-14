
n = input()
bef = 10

for i in range(len(n)):
    if int(n[i]) < bef:
        bef = int(n[i])
    else:
        print("No")
        exit()

print("Yes")