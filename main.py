# If, elif, else

print(1 + 0 == 1) # true
print( type(1) == type('1') ) # false

answer = input("41 + 1 = ")
if answer == str(42):
    print("You are right!")
elif answer == str(24):
    print("Almost")
else:
    print("You are wrong, try again")


age = int(input("Введите ваш возраст: "))
if (age > 0 and age < 18):
    print("You are a child")
elif ( (age >= 18 and age < 40) or (age >= 40 and age < 60) ):
    # Stupid condition to show how works the operator "or"
    print("You are an adult human")
elif (age >= 60 and age <= 100):
    print("You are a old human")
else:
    print("You are lying me -_-")


cars = ['lada', 'bmw', 'vw', 'kia', 'audi', 'fiat']
german_cars = ['bmw', 'vw', 'audi']

if 'lada' in cars:
    print("Yes, Lada is in the list")
else:
    print("No, Lada is not")


print("================= List + condition ===============")
for car in cars:
    if (car in german_cars):
        print(car + ' is German car')
    else:
        print(car + ' is not German')
