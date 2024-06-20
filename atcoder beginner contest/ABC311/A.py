n = int(input())
s = input()

a = set()

for i in range(n):
    a.add(s[i])
    if 'A' in a and 'B' in a and 'C' in a:
        print(i + 1)
        exit()