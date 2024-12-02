# Strings

full_name = "egoR semenov"

print(full_name.title()) # Egor Semenov
print(full_name.upper()) # EGOR SEMENOV
print(full_name.lower()) # egor semenov

print("Экранированный\nперенос строки")
print("Экранированный\tсимвол табуляции")
print("\"Экранированные кавычки\"")
print('\'Экранированные кавычки\'')
print('Экранированный слеш \\')

test_string = " ., ,, . . , ,, . . Python is cool .,, ., __ ,. ,.,  ,."
print("Без strip(): " + test_string)
print("С strip(): " + test_string.strip("., _"))

print("lstrip(): " + test_string.lstrip("., _")) # Python is cool .,, ., __ ,. ,.,  ,.
print("rstrip(): " + test_string.rstrip("., _")) # ., ,, . . , ,, . . Python is cool
