while True:
    inp = input('Insert something to check if it\'s a palindrome: ')
    inp_lower = inp.lower()
    palindrome = True
    for i, x in enumerate(inp_lower):
        # if len(inp) % 2 == 1 and i == len(inp) % 2:
        #     pass
        # elif
        if x != inp_lower[-i - 1]:
            palindrome = False
            break
    if palindrome:
        print(f"{inp} is a palindrome.")
    else:
        print(f"{inp} isn't a palindrome.")