### Конспект по уроку

Для того чтобы перехватить ошибку её нужно сначала создать, поэтому обратимся к файлу, которого не существует и попытаемся его прочитать:
```
file_for_error_path = "./unknown_file.txt"

file_for_error_obj = open(file=file_for_error_path, mode='r', encoding='utf8')
print(file_for_error_obj.read())
```
Получаем ошибку "FileNotFoundError: [Errno 2] No such file or directory: './unknown_file.txt'"  
  
Для отлавливания ошибок в python существует спецальный блок TRY+EXCEPT+ELSE+FINALLY:
```
try:
    print("Inside TRY")
    file_for_error_obj = open(file=file_for_error_path, mode='r', encoding='utf8')
except Exception:
    print("Inside EXCEPT")
else:
    print("Inside ELSE")
finally:
    print("Inside FINALLY")
```
  
Данный блок кода работает следующим образом:  
1. Пытается выполнить раздел try  
2.  
  - Если получает ошибку то выполняет раздел except  
  - Если не получает ошибку, то выполняет блок кода в разделе else  
3. В результате любого исхода выполняет код из раздела finally  
  
Для красоты примера, мы будем использовать в коде библиотеку sys, содержащую в себе системные команды. В нашем случае, нам понадобится только метод exit(), который прерывает выполлнение скрипта.  
Напишем бесконечный цикл, который будет спрашивать корректный относительный путь до файла для чтения до тех пор, пока пользователь не введет его:
```
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
```
*Сторока print(sys.exc_info()[1]) - выводит полученную ошибку в терминал*