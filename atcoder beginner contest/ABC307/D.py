from collections import deque

n = int(input())
s = list(input())

cnt = 0
place = deque()
del_l = deque()

for i in range(len(s)):
    if s[i] == "(":
        cnt += 1
        place.append(i)
    elif s[i] == ")":
        if cnt > 0:
            del_l.append((place[-1],i))
            del place[-1]
            cnt -= 1

min_del = 10**9
for i in range(len(del_l),0,-1):
    if min_del > del_l[i - 1][0]:
        min_del = del_l[i - 1][0]
        del s[del_l[i - 1][0]:del_l[i - 1][1] + 1]

print("".join(s))
