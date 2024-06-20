s = input()
t = input()

s_i = 0

for i in range(len(t)):
    if s[s_i] == t[i]:
        print(i + 1,end = " ")
        s_i += 1