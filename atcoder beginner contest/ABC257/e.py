def change_func(change_num):
    global flag,change,remaining,str_num
    for i in range(len(C)):
        if int(str_num[change_num]) < i + 1:
            if remaining - (C[i] - min_cos) >= 0:
                change = i + 1
                flag = True
    if flag:
        flag = False
        if change_num == 0:
            str_num = str(change) + str_num[1:]
        elif change_num == 8:
            str_num = str_num[:8] + str(change)  
        else:
            str_num = str_num[:change_num] + str(change) + str_num[change_num + 1:]
        remaining -= (C[i] - min_cos)
    if remaining > 0:
        if change_num > 7:
            return
        change_func(change_num+1)

N = int(input())
C = list(map(int,input().split()))
x = 0#合計コスト
#消費コスト順に並べる
cost_per = []
min_cos = 9999999999999999999
for i in range(len(C)):
    if min_cos > C[i]:
        min_cos = C[i]
        min_ob = i

cost_per = sorted(cost_per)
#入れれるだけ入れる
#7
flag = False
now_weight = 0
str_num = ""
while True:
    if now_weight + min_cos < N:
        now_weight += min_cos
        str_num += f"{min_ob + 1}"
    else :
        remaining = N - now_weight
        change_func(0)
        
        break

print(str_num)
