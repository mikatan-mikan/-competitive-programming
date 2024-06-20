s = input()

w_s = "".join(sorted(s))

if s == w_s:
    print("Yes")
else:
    print("No")