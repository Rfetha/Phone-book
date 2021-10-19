import os
import sys
from prettytable import PrettyTable


# Class Contact
class Contact(object):
    def __init__(self, name, surname, number):
        self.name = name
        self.surname = surname
        self.number = number


def show_list():
    t = PrettyTable(['Pos', 'Name', 'Surname', 'Number'])
    contacts.sort(reverse=False, key=name)

    for contact in contacts:
        t.add_row([contacts.index(contact) + 1, contact.name,
                   contact.surname, contact.number])

    print(t)


def add_contact():
    name = input("Name: ")
    surname = input("Surname: ")
    number = input("Phone number: ")
    contacts.append(Contact(name, surname, number))


def remove_contact():
    if not contacts:
        print("List is empty!")
    else:
        index = input(
            "Enter the position of the contact which is to be removed: ")
        contacts.pop(int(index) - 1)


def name(club):
    return club.name


def handling_input():
    print("(a - to add, s - to show, d - to delete, q - to quit)")
    entered = input("Please select desired action: ")
    input_dict[entered]()


def clear(): os.system('cls')
def quit_program(): sys.exit()


def main():
    global input_dict, contacts

    clear()
    contacts = []


    input_dict = {
        'a': add_contact,
        's': show_list,
        'd': remove_contact,
        'q': quit_program,
    }

    while True:
        handling_input()


if __name__ == '__main__':
    main()
