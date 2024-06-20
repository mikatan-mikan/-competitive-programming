s = input()

if s[0] == "<" and s[-1] == ">" and "<" not in s[1:-1] and ">" not in s[1:-1]:
    print("Yes")
else:
    print("No")