def string_reversal(string):
    new_string = ''
    for i, x in enumerate(string):
        new_string += string[-i - 1]
    return new_string

string = 'reverse'
print(f'{string} reversed is {string_reversal(string)}')