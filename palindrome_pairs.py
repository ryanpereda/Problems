# Given a list of words, find all pairs of unique indices such that the 
# concatenation of the two words forms a palindrome.

def palindrome_pairs(strs):
    list = []
    for i, str in enumerate(strs):
        j = i + 1
        while j < len(strs):
            if palindrome_check(strs[i] + strs[j]):
                list.append((strs[i], strs[j]))
            j += 1
    return list
        

def palindrome_check(str):
    for i, x in enumerate(str):
        if x != str[-i - 1]:
            return False
    return True

the_list = ['apple', 'lppa', 'ppl', 'one', 'no', 'n', '1-']
print(palindrome_pairs(the_list))