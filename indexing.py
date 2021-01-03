# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 16:31:37 2020

@author: Aneesha
"""

my_pet = 'Tammy'

# Prints the 'T'
print(my_pet[0])

# Prints the 'a'
print(my_pet[1])

# Prints the 'm'
print(my_pet[2])

# Prints the 'm'
print(my_pet[3])

# Prints the 'y'
print(my_pet[4])


def is_an_instructor(name):
    name = name.strip().lower()
    if name == 'aneesha' or name == 'shreya':
        print('Is an instructor')
    else:
        print('Not an instructor')
        
is_an_instructor('Aneesha')
is_an_instructor('aneesha')
is_an_instructor('AnEeShA                  ')




