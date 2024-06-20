
A,B,C,D,E = map(int,input().split())

num_list = [0 for i in range(13)]

num_list[A - 1] += 1
num_list[B - 1] += 1
num_list[C - 1] += 1
num_list[D - 1] += 1
num_list[E - 1] += 1

three_flag = False
two_flag = False

for i in range(len(num_list)):
    if num_list[i] == 3:
        three_flag = True
    elif num_list[i] == 2:
        two_flag = True

if three_flag == two_flag and two_flag == True:
    print("Yes")
else:
    print("No")