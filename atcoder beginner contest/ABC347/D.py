a,b,c = map(int,input().split())

c = bin(c)[2:]
#cが60桁になるように調整

c = c.zfill(60)

a_,b_ = [0 for _ in range(60)],[0 for _ in range(60)]
a_c,b_c = 0,0

same = set()
not_same = set()

for item in range(len(c)):
    if c[item] == '1':
        a_[item] = 0
        b_[item] = 1
        b_c += 1
        not_same.add(item)
    if c[item] == '0':
        a_[item] = 0
        b_[item] = 0
        same.add(item)

a_m = a - b
for i in same:
    if a_[i] == 0:
        a_[i] = 1
        b_[i] = 0
        a_c += 1
        b_c -= 1
    if a_c - b_c == a_m:
        for j in not_same:
            a_[j] = 1
            b_[j] = 1
            a_c += 1
            b_c += 1
            if a_c == a:
                print(int("".join(map(str,a_)),base=2),int("".join(map(str,b_)),base=2))
                exit()

print(-1)



