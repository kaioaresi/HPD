#!/usr/bin/env python3

age = int(input('Enter your age: '))
have_own_car = input('Do you own your car (y/n) ? ')

if age >= 21:
    if have_own_car == 'y':
        print('You are over 21 yeas old and own you car.')
    else:
        print('You are 21 years old and you do Not own your car.')
else:
    if have_own_car == 'y':
        print('You are yanger than 21 and you own your car.')
    else:
        print('You are yanger than 21 and you Do Not own your own car.')
