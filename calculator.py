def calculator(num1, num2, op):
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    elif op == '/':
        return num1 / num2
    else:
        return None
    
print(calculator(1, 2, '+'))
print(calculator(1, 2, '-'))
print(calculator(1, 2, '*'))
print(calculator(1, 2, '/'))
print(calculator(1, 2, 'a'))