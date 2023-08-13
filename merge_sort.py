import random

def merge_sort(list):
    if len(list) > 2:
        list1 = merge_sort(list[:len(list) // 2])
        list2 = merge_sort(list[len(list) // 2:])
        new_list = []
        while list1 or list2:
            if list1 and list2:
                if list1[0] <= list2[0]:
                    new_list.append(list1.pop(0))
                elif list2[0] <= list1[0]:
                    new_list.append(list2.pop(0))
            elif list1:
                new_list.append(list1.pop(0))
            elif list2:
                new_list.append(list2.pop(0))
        return new_list
    elif len(list) == 2:
        if list[0] < list[1]:
            return [list[0], list[1]]
        else:
            return [list[1], list[0]]
    elif len(list) == 1:
        return list


the_list = [0,3,2,7,4,6,6,5,3]
# print(the_list[:len(the_list) // 2])
# print(the_list[len(the_list) // 2:])
print(the_list)
the_list = merge_sort(the_list)
print(the_list)

new_list = []
for x in range(100):
    new_list.append(random.randint(0, 500))
print(new_list)
new_list = merge_sort(new_list)
print(new_list)