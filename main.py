# Catching of errors

file_for_error_path = "./unknown_file.txt"
"""
try:
    print("Inside TRY")
    file_for_error_obj = open(file=file_for_error_path, mode='r', encoding='utf8')
except Exception:
    print("Inside EXCEPT")
    print("!!! ERROR WAS FOUND !!!")
else:
    print("Inside ELSE")
    print(file_for_error_obj.read())
finally:
    print("Inside FINALLY")
"""

import sys
file_path = "./unknown_file.txt"

while True:
    try:
        file_obj = open(file_path, mode='r', encoding='utf8')
    except:
        print(sys.exc_info()[1])
        file_path = input("Enter correct file path: ")
    else:
        print(file_obj.read())
        sys.exit()
