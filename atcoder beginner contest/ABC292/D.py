import math

def count_ABCD(N):
    count = 0
    for D in range(1, N+1):
        if N % D == 0:
            M = N // D
            for A in range(1, int(math.sqrt(M))+1):
                if M % A == 0:
                    C = M // A
                    if (N - A*D) % C == 0 and (N - A*D) // C <= M:
                        count += 1
    return count

print(count_ABCD(4))

# import math

# def count_ABCD(N):
#     divisors = set()
#     for i in range(1, int(math.sqrt(N))+1):
#         if N % i == 0:
#             divisors.add(i)
#             divisors.add(N // i)
#     divisors = sorted(list(divisors))
#     return divisors

# div = count_ABCD(int(input()))

# if len(div) % 2 == 0:
#     add = 0
#     for i in div:
#         add += i
#     ans = 2 * (add / 2)
# else:
#     add = 0
#     for i in div:
#         add += i
#     ans = 2 * (add / 2) + 1
