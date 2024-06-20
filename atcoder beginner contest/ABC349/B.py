s = input()

cnt = [0 for _ in range(30)]
cnt_ = [0 for _ in range(1000)]

for i in range(len(s)):
    cnt[ord(s[i]) - 97] += 1

for i in range(30):
    cnt_[cnt[i]] += 1

for i in range(1,1000):
    if cnt_[i] != 0 and cnt_[i] != 2:
        print("No")
        exit()


print("Yes")