def insertion_sort(list):
    sorted = []
    for item in list:
        if not sorted:
            sorted.append(item)
        else:
            for j, sort in enumerate(sorted):
                if sort >= item:
                    sorted.insert(j, item)
                    break
                elif j == len(sorted) - 1:
                    sorted.append(item)
                    break
    return sorted

the_list = [2,1,4,6,3,0]
print(the_list)
insertion_sort(the_list)
print(the_list)
the_list = insertion_sort(the_list)
print(the_list)