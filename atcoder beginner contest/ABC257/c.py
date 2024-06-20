from math import sqrt

x_y_p_list = []
S = 1
N = int(input())
for i in range(N):
    x_y_p_list.append(list(map(int,input().split())))
#地点X_i,Y_iについてそれぞれの最寄りを保管(N*2)は最悪40000
x_y_want_list = []

#それぞれの最も近い物を探した
for i in range(N):
    min = 999999
    now_x = x_y_p_list[i][0]
    now_y = x_y_p_list[i][1]
    for j in range(N):
        if i == j :
            continue
        tmp = sqrt((x_y_p_list[j][0] - now_x)**2 + (x_y_p_list[j][1] - now_y)**2)
        if tmp < min:
            min = tmp
            min_j = j
    x_y_want_list.append([tmp,i,min_j])#i番目とj番目の組み合わせ保管

for i in range(len(x_y_want_list)):
    if x_y_p_list[i][2] * S >= abs(x_y_p_list[i][0] - x_y_p_list[x_y_want_list[i][2]][0]) + abs(x_y_p_list[i][1] - x_y_p_list[x_y_want_list[i][2]][1]):
        continue
    else:
        S+= 1

print(S)