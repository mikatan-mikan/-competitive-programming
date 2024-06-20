n = int(input())
a = list(map(int,input().split()))

a_ = {a[i]:i + 1 for i in range(n)}

now = -1

while True:
    try:
        print(a_[now],end = " ")
        now = a_[now]
    except:
        break
print()