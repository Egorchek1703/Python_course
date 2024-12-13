# Working with files

users_file = "./users.txt"
passwords_file = "./passwords.txt"

print(users_file, passwords_file)

users_file_obj = open(users_file, mode='r', encoding='utf8')
passwords_file_obj = open(passwords_file, mode='r', encoding='utf8')

print(users_file_obj.read())
print(passwords_file_obj.read())

users_file_obj.seek(0)
passwords_file_obj.seek(0)

for line in users_file_obj:
    print("Hello " + line.strip() + "!")


found_passwords = "./found_passwords.txt"
found_passwords_file_obj = open(found_passwords, mode='a', encoding='utf8')

substr_to_search = '_'
found_passwords_file_obj.write("\nFound passwords with: \"" + substr_to_search + "\"\n\n")

for num, line in enumerate(passwords_file_obj, 1):
    if "_" in line:
        print("Line " + str(num) + ": " + line)
        found_passwords_file_obj.write(line)

users_file_obj.close()
passwords_file_obj.close()
found_passwords_file_obj.close()