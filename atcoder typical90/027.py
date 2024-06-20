n = int(input())

s = [input() for _ in range(n)]

usr = set()

for i in range(len(s)):
    if s[i] in usr:
        continue
    usr.add(s[i])
    print(i + 1)