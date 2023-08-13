def bubble_sort(list):
    i = len(list)
    while i > 0:
        for j in range(i):
            if j + 1 < i:
                if list[j] > list[j+1]:
                    list[j], list[j+1] = list[j+1], list[j]
        i -= 1
    return list

the_list = [2,1,0,3,2,10,23,11]
print(the_list)
bubble_sort(the_list)
print(the_list)