N,X,Y,Z = map(int,input().split())

A = list(map(int,input().split()))#数学の点数
B = list(map(int,input().split()))#英語の点数

grades = []
grades_copy =[]
grades_copy_ = []

stu_list = []#合格済みの番号を保管

#個人の成績のリストを作る
for i in range(N):
    grades.append([A[i],B[i],A[i] + B[i],i + 1])
    grades_copy.append(grades[i])
    grades_copy_.append(grades[i])

for i in range(N):#数学の成績順にバブルソート
    for j in range(N - 1 , i , -1):
        if grades[j][0] > grades[j - 1][0]:
            grades[j],grades[j - 1] = grades[j - 1],grades[j]


for i in range(X):
    stu_list.append(grades[i])

for i in range(N):#英語の成績順にバブルソート
    for j in range(N - 1 , i , -1):
        if grades_copy[j][1] > grades_copy[j - 1][1]:
            grades_copy[j],grades_copy[j - 1] = grades_copy[j - 1],grades_copy[j]
count = 0
i = 0
if Y != 0:
    while True:
        if grades_copy[i] not in stu_list:
            stu_list.append(grades_copy[i])
            count += 1
        i += 1
        if count == Y:
            break

for i in range(N):#合計の成績順にバブルソート
    for j in range(N - 1 , i , -1):
        if grades_copy_[j][2] > grades_copy_[j - 1][2]:
            grades_copy_[j],grades_copy_[j - 1] = grades_copy_[j - 1],grades_copy_[j]
count = 0
i = 0
if Z != 0:
    while True:
        if grades_copy_[i] not in stu_list:
            stu_list.append(grades_copy_[i])
            count += 1
        i += 1
        if count == Z:
            break


stu_num = []
for i in range(len(stu_list)):
    stu_num.append(stu_list[i][3])
stu_num = sorted(stu_num)
for i in range(len(stu_list)):
    print(stu_num[i],end="\n")