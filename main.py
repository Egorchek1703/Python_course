# Arrays (lists)
#=============================== Part 1 ====================================

cities = ['Voronej', 'Moscow', 'ryazan', 'Smolensk', 'Taganrog']

name_of_list = list(range(0, 30))

print(name_of_list)

print( len(name_of_list) )

print( cities[2].title() ) # Ryazan
print( cities[2].upper() ) # RYAZAN
print( cities[3].lower() ) # smolensk

cities[2] = 'Ryazan_2'
print(cities) # выведет массив содержащий третим элементом строку 'Ryazan_2'


cities.append('Sevastopol\'')
print(cities)

cities.insert(2, 'Ryazan_1,5')
print(cities)

del cities[2] # удалит 'Ryazan_1,5'
print(cities)

cities.remove('Ryazan_2') # удалит 'Ryazan_2'
print(cities)

cities.sort()
name_of_list.sort(reverse=True)

print(cities)
print(name_of_list)

#=============================== Part 2 ====================================

cars = ['lada', 'VW', 'bmv', 'mersedes', 'kia', 'skoda']
for car in cars:
    print(car.upper())


my_number_list = list(range(0, 10))
for num in my_number_list:
    num = num * 2
    print(num)


cars = ['lada', 'VW', 'bmv', 'mersedes', 'kia', 'skoda']

german_cars = cars[1:4]
print("German cars: " + str(german_cars))

three_cars = cars[:3]
print("First 3 cars: " + str(three_cars))

some_cars = cars[2:]
print("Some cars: " + str(some_cars))

copy_of_list = cars[:]
print(copy_of_list)