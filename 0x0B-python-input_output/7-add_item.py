#!/usr/bin/python3
"""pass"""


import sys
import os.path
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


filename = "./add_item.json"

check_file = os.path.exists(filename)

if check_file is False:
    mylist = []
    with open(filename, "w") as file:
        file.write(str(mylist))

    number_of_arg = len(sys.argv)

    if number_of_arg > 1:
        for number in range(1, number_of_arg):
            mylist.append(sys.argv[number])
        save_to_json_file(mylist, "add_item.json")

else:
    mylist = load_from_json_file("add_item.json")

    number_of_arg = len(sys.argv)

    if number_of_arg > 1:
        for number in range(1, number_of_arg):
            mylist.append(sys.argv[number])
        save_to_json_file(mylist, "add_item.json")
