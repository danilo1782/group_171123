cities = "6..58київ\nоДеса     Львів\tжитоМИР      уЖгОрОд ХарКІВ       слАвУтИч74$:?$"

for char in cities:

    if not char.isalpha():
        cities = cities.replace(f'{char}', ' ')

cities_list = cities.title().split()

for city in cities_list:

    if city[-1] == 'a':
        city = f'{city.strip('a')}y'

    print(f'Я \U00002764 {city}')
