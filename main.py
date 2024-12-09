# Dictionaries

city_for_game = {
    'loc_x': 80,
    'loc_y': 120,
    'population': 12457,
    'name': 'Pythongrad',
    'eco_danger_lvl': 1,
    'is_a_capital': True,
    'health': 100,
}

print( city_for_game['name'].upper() ) # PYTHONGRAD


city_for_game['money'] = 120000000
print(city_for_game['money']) # 120000000

city_for_game['money'] = 125702000
print(city_for_game['money']) # 125702000


if (city_for_game['is_a_capital'] == True):
    city_for_game['eco_danger_lvl'] += 1

print(city_for_game)


print( city_for_game.keys() ) # dict_keys(['loc_x', 'loc_y', 'population', 'name', 'eco_danger_lvl', 'is_a_capital', 'health', 'money'])
print( city_for_game.values() ) # dict_values([80, 120, 12457, 'Pythongrad', 2, True, 100, 125702000])

# ============== Part 2 ==============
print("\n============== Part 2 ==============\n")

another_city = city_for_game.copy()
another_city['money'] = 700000

print(another_city)
print(city_for_game)


city_for_game['livers'] = ['Ivan Ivanov', 'Petr Petrov', 'John Doe']
city_for_game['location'] = {
    'x': 80,
    'y': 120,
}

print(city_for_game)