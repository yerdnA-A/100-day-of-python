list_of_strings = input().split(',')

list_numbers = [int(n) for n in list_of_strings]

par_list = [n for n in list_numbers if n % 2 == 0]

print(par_list)