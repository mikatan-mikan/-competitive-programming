S = input()

if S[0] != "0":
    print("No")
    exit()

r_1 = [S[6]]
r_2 = [S[3]]
r_3 = [S[7],S[1]]
r_4 = [S[4],S[0]]
r_5 = [S[8],S[2]]
r_6 = [S[5]]
r_7 = [S[9]]

pin = [r_1,r_2,r_3,r_4,r_5,r_6,r_7]
pin_bool = []

for i in pin:
    cnt = 0#倒れているピン数
    for j in i:
        if j == "0":
            cnt+=1
    if cnt == len(i):
        pin_bool.append(True)#全て倒れている
    else:
        pin_bool.append(False)#全ては倒れていない

#False (Trueがn個) Falseならスプリットなので
fir_dalse_flag = False
true_flag = False
for i in range(len(pin_bool)):
    if fir_dalse_flag == False and pin_bool[i] == False:
        fir_dalse_flag = True
    if fir_dalse_flag == True and pin_bool[i] == True:
        true_flag = True
    if true_flag == True and pin_bool[i] == False:
        print("Yes")
        exit()

print("No")
