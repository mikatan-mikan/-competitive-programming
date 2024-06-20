S = input()

flg = [False,False]

k = 0

for i in range(len(S)):
    if S[i] == "B":
        if (i + 1) % 2 == 0:
            if flg[0] == False:
                flg[0] = True
            else:
                print("No")
                exit()
        else:
            if flg[1] == False:
                flg[1] = True
            else:
                print("No")
                exit()
    if S[i] == "R":
        if k == 1:
            print("No")
            exit()
        k += 1
    if S[i] == "K":
        if k != 1:
            print("No")
            exit()
        else:
            k += 1
print("Yes")