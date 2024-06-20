s = input()

f = False

for i in s:
    if i != "|" and f == False:
        print(i,end = "")
    elif i == "|" and f == False:
        f = True
    elif i == "|" and f == True:
        f = False

print()