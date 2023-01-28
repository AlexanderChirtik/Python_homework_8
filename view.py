def show_menu() -> int:
    print("\n" + "=" * 20)
    print("Выберите необходимое действие")
    print("1. Найти сотрудника")
    print("2. Сделать выборку сотрудников по должности")
    print("3. Сделать выборку сотрудников по зарплате")
    print("4. Добавить сотрудника")
    print("5. Удалить сотрудника")
    print("6. Обновить данные сотрудника")
    print("7. Экспортировать данные в формате json")
    print("8. Экспортировать данные в формате csv")
    print("9. Закончить работу")
    return int(input("Введите номер необходимого действия: "))


def find_people():
    return input('Who do you want to find ')



def add_new_personal():
    name = input('Name: ')
    surname = input('Surname: ')
    age = input('Age: ')
    position = input('Position: ')
    salary = input('Salary: ')
    return name, surname, age, position, salary

def delete_people():
    return input('Who do you want to delete ')

def update_data():
    return input('Who do you want to update ')

def export():
    csvFilePath = input('Enter csvFilePath ')
    jsonFilePath = input('Enter jsonFilePath ')
    return csvFilePath, jsonFilePath