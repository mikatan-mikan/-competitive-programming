s = input()

ml = 0

for start in range(len(s)):
    for fin in range(start + 1,len(s) + 1):
        #回文を判定
        if s[start:fin] == s[start:fin][::-1]:
            ml = max(ml,fin - start)

print(ml)