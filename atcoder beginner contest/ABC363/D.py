
n = int(input())

length = 1
while True:
    half_length = (length + 1) // 2
    if length % 2 == 0:
        count = 9 * 10 ** (half_length - 1)
    else:
        count = 9 * 10 ** (half_length - 1)
    
    if n <= count:
        break
    
    n -= count
    length += 1

half_length = (length + 1) // 2
start = 10 ** (half_length - 1)
num = start + n - 2
half_str = str(num)

if length % 2 == 0:
    ans = int(half_str + half_str[::-1])
else:
    ans = int(half_str + half_str[-2::-1])
print(ans)