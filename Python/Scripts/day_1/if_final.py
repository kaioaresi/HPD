age = int(input('Enter your age: '))
have_own_car = input('Do you have a car (y/n) ?: ')

if (age > 21) and (have_own_car == 'y'):
    print('You are over 21 years old and own your car.')
if (age > 21) and (have_own_car == 'n'):
    print('You are over 21 old and you do Not own your car')
if (age == 21) and (have_own_car == 'y'):
    print('You are 21 years old and own your car.')
if (age < 21) and (have_own_car == 'y'):
    print('You are yanger than 21 and own your car.')
if (age < 21) and (have_own_car == 'n'):
    print('You are yanger than 21 and you Not own your car.')
