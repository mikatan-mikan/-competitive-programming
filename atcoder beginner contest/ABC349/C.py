s = input()
t = input()

if t[-1] == "X":
    t = t[:-1]

s_ptr = 0
t_ptr = 0

while True:
    if s[s_ptr] == t[t_ptr].lower():
        s_ptr += 1
        t_ptr += 1
        if t_ptr == len(t):
            print("Yes")
            exit()
    else:
        s_ptr += 1
        if s_ptr == len(s):
            print("No")
            exit()