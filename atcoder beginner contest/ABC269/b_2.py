S = []
for i in range(10):
    S.append(input())

def wid():
    flag = 0
    for i in range(len(S)):
        if flag == 1:
            break
        for j in range(len(S)):
            if S[i][j] == "#" and flag == 0:
                first_point = j + 1
                flag = 1
            elif flag == 1 and S[i][j] == ".":
                second_point = j
                flag = 2
    if flag == 1:
        second_point = 10
    print(first_point,second_point)
def hei():
    flag = 0
    for i in range(len(S[0])):
        if flag == 1:
            break
        for j in range(len(S)):
            if S[j][i] == "#" and flag == 0:
                first_point = j + 1
                flag = 1
            elif S[j][i] == "." and flag == 1:
                second_point = j
                flag = 2
    if flag == 1:
        second_point = 10
    print(first_point,second_point)

#縦走査
hei()
wid()