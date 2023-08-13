def factorial_function(num):
    result = 1
    while num > 1:
        result *= num
        num -= 1
    return result

def factorial_recursive(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial_recursive(num-1)
    
for i in range(10):
    print(f'{i}: {factorial_function(i)}, {factorial_recursive(i)}')