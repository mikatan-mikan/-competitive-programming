n = int(input())
s = input()
t = input()

for i in range(n):
    if (s[i] == t[i] or (s[i] == '1' and t[i] == 'l') or (t[i] == '1' and s[i] == 'l') or (s[i] == '0' and t[i] == 'o') or (t[i] == '0' and s[i] == 'o')):
        continue
    print('No')
    exit()
print('Yes')