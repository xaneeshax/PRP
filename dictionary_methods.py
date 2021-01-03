# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 12:29:00 2020

@author: Aneesha
"""

office = {
    
    'Jim' : ['pranks', 'sales', 'basketball'],
    'Dwight' : ['beets', 'sales', 'bears', 'battlestar galactica'],
    'Michael' : ['basketball', 'sales', 'pranks'],
    'Pam' : ['pranks', 'beets', 'art'],
    'Angela': ['accounting', 'beets', 'cats']

    }

# .keys() Method
'''
for key in office.keys():
    print(key)
'''

# .values() Method

for activities in office.values():
    for activity in activities:
        print(activity)


# .items() Method
for key, value in office.items():
    print(key)
    print(value)
    print()

