# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 13:42:01 2020

@author: Aneesha
"""

my_number = 3

def is_it_odd(number):
    if number % 2 == 1:
        print('yes, it\'s odd!')
    else:
        print('hey its even')
        
def is_odd(number):
    if number % 2 == 1:
        return 'odd'
    else:
        return 'even'
    
    
print(is_it_odd(my_number))