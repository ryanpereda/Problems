def is_prime_number(num):
    if num == 0 or num == 1:
        return False
    is_prime = True
    i = 2
    while i <= num // 2:
        if num % i == 0:
            is_prime = False
            break
        i += 1
    return is_prime

for number in range(100):
    if is_prime_number(number):
        print(f"{number} is a prime number.")
    else: 
        print(f"{number} isn't a prime number.")