with open('Day 26/file1.txt', 'r') as file_1:
    contents_1 = file_1.readlines()

with open('Day 26/file2.txt', 'r') as file_2:
    contents_2 = file_2.readlines()

compare = [n_1 for n_1 in contents_1 if n_1 in contents_2]
print(compare)