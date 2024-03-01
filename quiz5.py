def fast_mod_exp(val, power, mod):
    result = 1
    while power > 0:
        if power % 2 == 1:
            result = (result * val) % mod
        val = (val * val) % mod
        power = power // 2
    return result


def find_mod_inverse(val, mod):
    for i in range(1, mod):
        if (val * i) % mod == 1:
            return i
    return None


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def find_relative_primes(num):
    prime_list = []
    for i in range(1, num):
        if gcd(i, num) == 1:
            prime_list.append(i)
    return len(prime_list)


def find_prime_factors(num):
    for i in range(2, num):
        if num % i == 0:
            return i, num // i


def rsa_find_d(e, N):
    p, q = find_prime_factors(N)
    phi = (p - 1) * (q - 1)
    d = find_mod_inverse(e, phi)
    return d


print("q1", fast_mod_exp(2, 345, 31))
print("q2", fast_mod_exp(2, 31, 11))
print("q3", fast_mod_exp(3, 2003, 5))
print("q4", find_mod_inverse(13, 22))
print("q5", (fast_mod_exp(2, 20, 7) + fast_mod_exp(4, 40, 7) +
      fast_mod_exp(5, 50, 7) + fast_mod_exp(6, 60, 7)) % 7)

print("q6", find_relative_primes(143))
print("q7", gcd(22608, 10206))
print("q8", rsa_find_d(7, 133))  # p, q = 7, 19
print("q9", fast_mod_exp(5, rsa_find_d(7, 133), 133))
print("q10", fast_mod_exp(5, 3, 33))
