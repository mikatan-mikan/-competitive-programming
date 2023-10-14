from collections import deque
S = deque()
S_int = deque()
N = int(input())
for i in range(N):
    S.append(input())

end_sec = [10,10,10,10,10,10,10,10,10,10]

flag = True

time = 0

range_list = list(range(10000))
range_str_list = ["0","1","2","3","4","5","6","7","8","9"]

count = [N,N,N,N,N,N,N,N,N,N]

for time in range_list:#絶対に10秒で一巡する(現在時刻)
    time_point = (time % 10)#0から数えるから+1しなくて良い
    for check_num in range_str_list:
        check_num_int = int(check_num)
        for i in S:#全リールを走査
            if i[time_point] == check_num:#もし探している数字であれば
                count[check_num_int] -= 1
                
                if count[check_num_int] == 0:#count が 0  ==  全てのリールが探している数字であれば -> それぞれの数字に対してcountが必要
                    end_sec[check_num_int] = time
                    flag = False
                    break
                else:
                    break
        if flag == False:
            flag = True
            break

print(min(end_sec))
#0123456789
