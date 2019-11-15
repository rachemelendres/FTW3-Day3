##  Euler Exercise 3 - Largest Prime Factor

def largest_prime_fac(number):
    n = number
    x = 2
    prime_factors = []
    while x <= n:
        if n % x == 0:
            prime_factors.append(x)
            n /=x
        else:
            x += 1
    return "The largest prime factor of {} is {}.".format(number, max(prime_factors))
print(largest_prime_fac(600851475143))
