from collections import Counter
from math import isqrt

def countSquareStrings(S):
    digit_count = Counter(S)  # Sの各数字の出現回数をカウント
    
    def dfs(s, i):
        if i == len(S):
            num = int(s)
            sqrt_num = isqrt(num)
            if sqrt_num * sqrt_num == num:
                return 1
            return 0
        
        count = 0
        for d in digit_count:
            if digit_count[d] > 0:
                digit_count[d] -= 1
                count += dfs(s + d, i + 1)
                digit_count[d] += 1
        return count
    
    return dfs("", 0)

# テスト用の例
S = "8694027811503"
result = countSquareStrings(S)
print(result)