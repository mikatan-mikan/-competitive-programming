
n = int(input())

n -= 1

ans = 0
base = 1

while n > 0:
    ans += (n % 5) * base
    n //= 5
    base *= 10

ans = str(ans)

#前から置換する
cg = {0: 0, 1: 2, 2: 4, 3: 6, 4: 8}

for i in ans:
    print(cg[int(i)],end="")

print()