print('~' * 40)
name = 'Danilo'
age = 41
salary = 25678
retirement_age = 65
months_in_a_year = 12
dollar_exchange_rate = 37.3
car_cost = 31500

years_until_retirement = retirement_age - age
print(f'{years_until_retirement=}')

money_until_retirement = months_in_a_year * years_until_retirement * salary
print(f'{money_until_retirement=}')

earned_in_dollars = money_until_retirement / dollar_exchange_rate
print(f'{earned_in_dollars=}')
less_earned_in_dollars = round(earned_in_dollars)
print(round(earned_in_dollars,3))

quantity = round(earned_in_dollars / car_cost)
print(f'{quantity=}')
less_quantity = round(quantity,1)

reality = """"я, Данило, зможу заробити лише __198264.45__ доларів \n що вистачить лише на __6__ тойот, \n мене це не влаштовує, \n тому я буду змінювати своє життя \n і буду завзято вивчати програмування"""
print(reality)
