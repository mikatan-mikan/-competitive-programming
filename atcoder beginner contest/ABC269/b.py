S = []
for i in range(10):
    S.append(input())

fir_flag = False
break_flag = False
print_flag = False

##縦走査
for i in range(len(S)):
    fir_flag = False
    break_flag = False
    for j in range(len(S[i])):
        if fir_flag == False and S[j][i] == "#":
            first_place = j + 1
            fir_flag = True
        if fir_flag == True and S[j][i] == ".":
            end_place = j
            print(first_place,end_place)
            print_flag = True
            break_flag = True
        if break_flag:
            break
    if break_flag:
        break

if print_flag == False:
    print(1,10)

fir_flag = False
break_flag = False
for i in range(len(S)):
    fir_flag = False
    for j in range(len(S[i])):
        if fir_flag == False and S[i][j] == "#":
            first_place = j + 1
            fir_flag = True
        if fir_flag == True and S[i][j] == ".":
            end_place = j
            print(first_place,end_place)
            exit()

print(1,10)