def largest_element(list):
    largest = list[0]
    for i in list:
        if i > largest:
            largest = i
    return largest

print(largest_element([0,3,5,2]))