n = int(input())

now = 10 ** 6

#x^3 == Kならなので10**6程度回せばよい
while True:
    if now ** 3 > n:
        now -= 1
        continue
    if str(now ** 3) == str(now ** 3)[::-1]:
        print(now ** 3)
        break
    now -= 1