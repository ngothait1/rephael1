# Python course - level 3 - Advanced
# Lesson 59 - Midterm Project - Revision 1
# Author: Rephael Sintes

# Polymorphism Edition

import os
import json
import pandas as pd
from utils import isDigit
from Person import Person
from Student import Student
from Employee import Employee


def printMenu():
    print("1. Save a new entry")
    print("2. Search by ID")
    print("3. Print ages average")
    print("4. Print all Names")
    print("5. Print all IDs")
    print("6. Print all entries")
    print("7. Print entry by index")
    print("8. Save all data")
    print("9. Exit")


def saveNewEntry(entries_lst, ids_dict):
    entryType = input("Type of entry: 1. Person, 2. Student, 3. Employee: ")
    while entryType not in ["1", "2", "3"]:
        entryType = input("Type of entry: 1. Person, 2. Student, 3. Employee: ")

    id_number = input("ID: ")
    if isDigit(id_number, "ID"):
        id_number = int(id_number)
    else:
        return 0
    if id_number in ids_dict:
        existing_entry = entries[ids_dict[id_number]]
        existing_name = f"'name': '{existing_entry.getName()}'"
        existing_age = f"'age': {existing_entry.getAge()}"
        print(f"Error: ID already exists: {{{existing_name}, {existing_age}}}")
        return 0

    name = input("Name: ")
    if not name.isalpha():
        print(
            f"Error: Name must contain only alphabetical characters. {name} is not alphabetical"
        )
        return 0

    age = input("Age: ")
    if isDigit(age, "Age"):
        age = int(age)
    else:
        return 0

    if entryType == "1":
        entries_lst.append(Person(id_number, name, age))
    elif entryType == "2":
        entries_lst.append(Student(id_number, name, age, user_input=True))
    else:
        entries_lst.append(Employee(id_number, name, age, user_input=True))

    ids_dict[id_number] = len(entries_lst) - 1
    print(f"ID [{id_number}] saved successfully")
    return age


def searchByID(entries_lst):
    id_to_search = input("Please enter the ID you want to look for: ")
    if isDigit(id_to_search, "ID"):
        id_to_search = int(id_to_search)
    else:
        return

    if id_to_search not in ids_to_indices:
        print(f"Error: ID {id_to_search} is not saved")
        return

    index = ids_to_indices[id_to_search]
    printEntryData(index, entries_lst[index])


def printAgesAverage(entries_num, ages_sum_value):
    if entries_num == 0:
        print(0.0)
    else:
        print(ages_sum_value / entries_num)


def printAllNames(entries_lst):
    for index, person in enumerate(entries_lst):
        print(f"{index}. {person.getName()}")


def printAllIDs(entries_lst):
    for index, person in enumerate(entries_lst):
        print(f"{index}. {person.getID()}")


def printAllEntries():
    for index, person in enumerate(entries):
        printEntryData(index, person, "\n\n")


def printEntryByIndex(last_index, entries_lst):
    index_to_print = input("Please enter the index of the entry you want to print: ")
    if isDigit(index_to_print, "Index"):
        index_to_print = int(index_to_print)
    else:
        return

    if index_to_print > last_index:
        print(f"Error: Index out of range. The maximum index allowed is {last_index}")
        return

    printEntryData(index_to_print, entries_lst[index_to_print])


def saveAllData(entries_lst):
    output_file_name = input("What is your output file name? ")
    dicts_lst = [entry.getDictionary() for entry in entries_lst]
    df = pd.DataFrame(dicts_lst)
    df.to_csv(output_file_name, index=False)


def exitProgram():
    to_exit = input("Are you sure? (y/n)")
    while to_exit not in ["y", "n"]:
        to_exit = input("Are you sure? (y/n)")
    if to_exit == "y":
        exit(0)


def printEntryData(index, person, end="\n"):
    person.printMyself(str(index), end)


entries = []
ids_to_indices = {}
ages_sum = 0

entries.append(Person(101, "Rephael", 27))
entries.append(Person(102, "Nadav", 36))
entries.append(Person(103, "Sapir", 24))
entries.append(Student(104, "Alex", 29, "Math", 2, 89))
entries.append(Student(105, "James", 31, "Physics", 3, 79))
entries.append(Employee(106, "Galit", 42, "Dentist", 32000))
entries.append(Employee(107, "Sean", 39, "Register", 7500))

ids_to_indices[101] = 0
ids_to_indices[102] = 1
ids_to_indices[103] = 2
ids_to_indices[104] = 3
ids_to_indices[105] = 4
ids_to_indices[106] = 5
ids_to_indices[107] = 6

ages_sum += 27
ages_sum += 36
ages_sum += 24
ages_sum += 29
ages_sum += 31
ages_sum += 41
ages_sum += 39


while True:
    printMenu()
    option = input("Please enter your option:")
    if isDigit(option, "Option"):
        option = int(option)
    else:
        continue

    if option < 1 or option > 9:
        print(f"Error: Option {option} does not exist. Please try again")
        continue
    elif option == 1:
        ages_sum += saveNewEntry(entries, ids_to_indices)
    elif option == 2:
        searchByID(entries)
    elif option == 3:
        printAgesAverage(len(entries), ages_sum)
    elif option == 4:
        printAllNames(entries)
    elif option == 5:
        printAllIDs(entries)
    elif option == 6:
        printAllEntries()
    elif option == 7:
        printEntryByIndex(len(entries) - 1, entries)
    elif option == 8:
        saveAllData(entries)
    elif option == 9:
        exitProgram()
    input("Press enter to continue")
