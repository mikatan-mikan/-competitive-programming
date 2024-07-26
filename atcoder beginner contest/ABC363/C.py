from itertools import permutations
from functools import lru_cache


n, k = map(int, input().split())
s = input()

@lru_cache(maxsize=None)
def is_condition(s):
    return s == s[::-1]
def is_(s, k):
    for i in range(len(s) - k + 1):
        if is_condition(s[i:i + k]):
            return True
    return False

perm = set(permutations(s))

cnt = 0
for p in perm:
    if not is_(p, k):
        cnt += 1

print(cnt)