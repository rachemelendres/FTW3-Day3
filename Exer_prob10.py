# Euler Exercise 10: Program to a find summation of all primes

def summation_primes(x):
    prime_factors = 0
    for n in range(1, x+1):
        if n>1:
            for y in range(2,n):
                if n%y ==0:
                    break
            else:
                prime_factors+=n
    return "The prime numbers between 1 and {} are {}.".format(x, prime_factors)
print(summation_primes(2000000))