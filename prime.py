## A program to check if a given number is a Prime Number

def prime_checker(number): # function is defined to check an inputted number
    if number <=1:
        return "{} is NOT a prime number".format(number) # All negative numbers, 0, and 1 are NOT prime numbers
    else: # proceed to this condition if numbers are greater than 1
        x = 2
        while x < number: # iterate all numbers below the inputted number
            if number % x==0: # check if inputted number is divisible by any number below it, aside from 1
                return "{} is NOT a prime number".format(number)
            x+=1
        return "{} is a prime number".format(number) # if inputted number is only divisible by itself and 1
print(prime_checker(99991))
print(prime_checker(999979))
print(prime_checker(88))