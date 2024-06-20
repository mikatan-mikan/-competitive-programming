n = int(input())

#decimal
from decimal import Decimal
a = list(map(Decimal,input().split()))

avg_a = Decimal(sum(a)) / Decimal(n)


plus = Decimal(0)
minus = Decimal(0)

for i in range(n):
    if a[i] < avg_a:
        plus += avg_a - Decimal(a[i])
    else:
        minus += Decimal(a[i]) - avg_a

print((plus + minus) // 2)