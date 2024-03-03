import pandas

'''with open('Day 25/weather_data.csv', 'r') as data_file:
    data = data_file.readlines()
    print(data)'''

'''import csv

with open('Day 25/weather_data.csv') as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != 'temp':
            temperatures.append(int(row[1]))
    print(temperatures)'''

'''data = pandas.read_csv('Day 25/weather_data.csv')'''

'''print(type(data))
print(data['temp'])'''

'''data_dict = data.to_dict()
print(data_dict)'''

'''temp_list = data["temp"].to_list()
print(temp_list)'''

'''average = sum(temp_list) / len(temp_list)
print(f'{average:.2f}')'''

'''print(data['temp'].mean())

print(max(data['temp']))
print(data['temp'].max())

print(data['condition'])
print(data.condition)'''

'''print(data[data.day == 'Monday'])
print(data[data.temp == data.temp.max()])'''

'''monday = data[data.day == 'Monday']
monday_temp = monday.temp[0]
monday_temp_F = monday_temp * 9/5 + 32
print(monday_temp_F)'''

'''data_dict = {
    "students" : ['Any', 'Sam', 'Dean'],
    "scores" : [76, 100, 38]
}

data = pandas.DataFrame(data_dict)
data.to_csv('Day 25/new_data.csv')'''

data = pandas.read_csv('Day 25/squirrel_data.csv')

gray_squirrel_count = len(data[data['Primary Fur Color'] == 'Gray'])
red_squirrel_count = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black_squirrel_count = len(data[data['Primary Fur Color'] == 'Black'])

data_dict = {
    'Fur Color' : ['Gray', 'Cinnamon', 'Black'],
    'Count' : [gray_squirrel_count, red_squirrel_count, black_squirrel_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv('Squirrel_count.csv')