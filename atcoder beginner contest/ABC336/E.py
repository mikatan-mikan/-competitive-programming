n = int(input())
a = list(map(int, input().split()))

a_m = [0] * (n + 1)
a_st = [0] * (n + 1)

for i in range(1, n + 1):
    a_m[i] = a_m[i - 1] + 1
    a_st[i] = a_st[i - 1]
    if (i - 1) - a_st[i] >= a[i - 1]:
        a_st[i] = i - 1 - a[i - 1]
        a_m[i] = i - a_st[i]

a_m_back = [0] * (n + 2)
a_st = [n - 1] * (n + 2)

for i in range(n, 0, -1):
    a_m_back[i] = a_m_back[i + 1] + 1
    a_st[i] = a_st[i + 1]
    if ((n - 1) - a_st[i]) - (n - i) >= a[i - 1]:
        a_st[i] = i - 1 - a[i - 1]
        a_m_back[i] = i - 1 - a_st[i]

max_num = -1
for i in range(1, n + 1):
    if max_num < min(a_m[i], a_m_back[i]):
        max_num = min(a_m[i], a_m_back[i])

print(max_num)