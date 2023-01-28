import csv
import json


def find_personal(key):
    with open('members.cvs', 'r') as file:
        data = file.read().split('\n')
        for i in data:
            if i.count(key):
                name, surname, age, position, salary = i.split(';')
                return print(f'{name} {surname} {age} {position} {salary}')
            else:
                return print('Not found')

def new_personal(card):
    name, surname, age, position, salary = card
    with open('members.cvs', 'a') as data:
        data.write(f'{name};{surname};{age};{position};{salary}\n')
    return 'New member was create'

def delete_personal(key):
    with open('members.cvs', 'r') as file:
        data = file.read().split('\n')
        for i in data:
            if i.count(key):
                data.remove(i)
                return print(f'Data deleted')
            else:
                return print('Not found')




def export_json(csvFilePath, jsonFilePath):
        jsonArray = []
        with open(csvFilePath, encoding='utf-8') as csvf:
            csvReader = csv.DictReader(csvf)
            for row in csvReader:
                jsonArray.append(row)
        with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
            jsonString = json.dumps(jsonArray, indent=4)
            jsonf.write(jsonString)


def export_csv():
    with open('data_json.csv', 'w') as fp:
        json.dump('members.cvs')


def update_data(key):
    with open('members.cvs', 'r') as file:
        data = file.read().split('\n')
        for i in data:
            if i.count(key):
                name, surname, age, position, salary = i.split(';')
                list = [name, surname, age, position, salary]
                point = input('What do you want to update: name, surname, age, position, salary ')
                new_data = input('Enter new data ')
                for i in list:
                    if i == point:
                        with open('members.cvs', 'w') as data:
                            list[point]= new_data
                return print('Data changed')
            else:
                return print('Not found')