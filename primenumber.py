from os import MFD_ALLOW_SEALING


def is_prime_with_flag(num):
    if num <=1:
        return False
    flag = True
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            flag = False
            break
        return flag
number =int(input("Enter a number:"))
if is_prime_with_flag(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")