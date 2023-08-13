string1 = ''
string2 = ''

def check_anagrams(str1, str2):
    if str1 == '' and str2 == '':
        return False
    elif len(str1) != len(str2):
        return False
    else:
        for letter1 in str1:
            found = False
            for letter2 in str2:
                if letter1 == letter2:
                    str1 = str1.replace(letter1, '', 1)
                    str2 = str2.replace(letter2, '', 1)
                    print(str1, str2)
                    found = True
                    break
            if not found:
                print(f'failed on {letter1}')
                return False
        return True

print(check_anagrams('master', 'tamese'))