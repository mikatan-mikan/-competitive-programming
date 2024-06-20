def calculate_remainder(n):
    MOD = 998244353
    power_of_ten_n = pow(10, n, MOD)
    power_of_ten_n_squared = pow(10, n * n, MOD)
    numerator = (power_of_ten_n_squared - 1 + MOD) % MOD
    denominator = (power_of_ten_n - 1 + MOD) % MOD
    denominator_inverse = pow(denominator, MOD - 2, MOD)  # Using Fermat's Little Theorem
    result = n * numerator % MOD * denominator_inverse % MOD
    return result

# Test with the provided example
n = 10
print(calculate_remainder(n))