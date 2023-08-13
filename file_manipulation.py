from word_count import word_count

file_path = 'the_file.txt'
file2_path = 'the_other_file.txt'
with open(file_path, 'w') as file:
    file.write('apples bananas')

with open(file_path, 'r') as file:
    content = file.read()
    with open(file2_path, 'w') as file2:
        the_dict = word_count(content)
        for i in the_dict:
            print(f'{i} : {the_dict[i]}')
            file2.write(f'{i} : {the_dict[i]}\n')
        
