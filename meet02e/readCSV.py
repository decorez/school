import csv

with open('data.csv','r') as file:
    csv_reader = csv.DictReader(file)

    for row in csv_reader:
        name = row['name']
        age = row['age']
        print(f'Name: {name}, age: {age}')