s = input()

str_ = set()

for i in range(len(s)):
    for j in range(i + 1,len(s) + 1):
        str_.add(s[i:j])

print(len(str_))