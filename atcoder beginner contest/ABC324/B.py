n = int(input())


while True:
    if n == 1:
        print("Yes")
        exit()
    if n % 2 == 0:
        n /= 2
    elif n % 3 == 0:
        n /= 3
    else:
        print("No")
        exit()