n=int(input())

ppls = [0,0]
watch = []
poison_ = [0]#対応表

for i in range(1,101,3):
    watch += [[i,i + 1], [i + 1, i + 2]]

for i in range(1,101):
    poison_.append(poison_[-1] + 1)
    if i % 2 == 0:
        poison_[-1] += 1

for i in range(2,101):
    ppls.append(ppls[-1] + 1)
    if i % 3 - 1 == 0:
        ppls[-1] -= 1

if n == 2:
    print("1 1")
    ans = input()
    if ans[0] == "0":
        print("1")
    else:
        print("2")
    exit()

#偶数人ならずらして渡す

for i in range(ppls[n] - 1):
    print("2 ",end = "")
    print(*watch[i],end = "\n")
if ppls[n] % 2 == 0:
    print("2 ",end = "")
    print(*watch[ppls[n] - 1],end = "\n")
else:
    print("2 ",end = "")
    print(watch[ppls[n] - 1][0] - 1,watch[ppls[n] - 1][1] - 1,end = "\n")
ans = input()
poison = []

for i in range(len(ans)):
    if ans[i] == "0":
        continue
    else:
        poison.append(i)

if len(poison) == 0:
    print(n)
if len(poison) == 1:
    print(poison_[poison[0] + 1])
if len(poison) == 2:
    print(poison_[poison[0] + 1] + 1)