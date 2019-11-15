## Program to check strings, integers, and lists for palindromes

def palindrome_checker(enter):

    if type(enter) == list or type(enter) == str:
        if enter == enter[::-1]:
            return "{} is a palindrome.".format(enter)
        else:
            return "{} is NOT a palindrome.".format(enter)
    else:
        num_to_string = str(enter)
        if num_to_string == num_to_string[::-1]:
            return "{} is a palindrome.".format(enter)
        else:
            return "{} is NOT a palindrome.".format(enter)

print(palindrome_checker(["d", "e", "i", "f", "i", "e", "d"]))
print(palindrome_checker('civic'))
print(palindrome_checker('madam'))
print(palindrome_checker([1,2,3,4,5]))
print(palindrome_checker(34539))
print(palindrome_checker([-1,[2,1],-1]))
print(palindrome_checker(["choco", 23, "choco"]))
