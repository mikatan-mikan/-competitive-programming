L1,R1,L2,R2 = map(int,input().split())

list_ = [0 for _ in range(100)]

for i in range(L1,R1):
    list_[i - 1] = 1
for i in range(L2,R2):
    if list_[i - 1] == 1:
        list_[i - 1] = 2
    else:
        list_[i - 1] = 1
cnt = 0
for i in range(100):
    if list_[i] == 2:
        cnt += 1

print(cnt)