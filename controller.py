import view as v
import modul as m
import os

def menu():
    points = [find_member,sam_position,sam_salary,add_member,del_member,update,export_json,export_csv,exit_of_program]
    return points[v.show_menu() - 1]()


def create_base():
    if (os.path.isfile('members.cvs') == False):
       with open('members.cvs', 'w') as file:
           file.write('')

def find_member():
    return m.find_personal(v.find_people())


def sam_position():
    return print('Information not found')

def sam_salary():
    return print('Information not found')


def add_member():
    return print(m.new_personal(v.add_new_personal()))

def del_member():
    return m.delete_personal(v.delete_people())

def update():
    return m.update_data(v.update_data())

def export_json():
    return m.export_json(v.export())

def export_csv():
    return export_csv()

def exit_of_program():
    return print('The program is closed')

