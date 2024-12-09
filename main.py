# Input

name = input("Write your name: ")
print("Привет " + name + "!")

a = input("a = ") # введем 4
b = input("b = ") # введем 2
print(a + b) # 42
print( int(a) + int(b) ) # 6


password = ''
while True:
    password = input('Password: ')
    if(password != '123'):
        print('Password "' + password + '" is not correct')
    else:
        print('You are authorized!')
        break

print('Cycle has been finished')