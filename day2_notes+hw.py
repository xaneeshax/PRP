# -*- coding: utf-8 -*-
"""Day2 Notes+HW.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gNlu3pkBngN0vm1Qri_o1N7aksTwjwD5

# DAY 2 (Reminder: Select "Save Copy to Drive")

Setup
1. Google Collab Intro
2. Github Setup


Content
1. List Comprehension
2. Dictionaries
3. Intro to Dataframes

# HW

1. Create a Github (if you don't already have one)

2. Solve the "Network Questions"

3. Submit the shareable link on Google Classroom

# List Comprehension

Create a list with the square of all odd numbers from 1 through 50
"""

final_list = []
for i in range(1,50):
  if i % 2 == 1:
    final_list.append(i**2)

print(final_list)

# numbers from 1 through 50

one_to_fifty = [i for i in range(1,51)]

# squares of numbers from 1 through 50
squares_one_to_fifty = [i**2 for i in range(1,51)]

# odd squares of numbers 1 through 50
odd_squares_one_to_fifty = [i**2 for i in range(1,51) if i % 2 == 1]

print(odd_squares_one_to_fifty)

"""# Dictionaries

# The Office
"""

# Why Lists do the Job -  but not as well
jim = ['pranks', 'sales', 'basketball']
pam = ['pranks', 'beets', 'art']

characters_list = [jim, pam]

people_who_like_pranks = 0
for character_interests in characters_list:
  if 'pranks' in character_interests:
    people_who_like_pranks += 1

office = {
    
    'Jim' : ['pranks', 'sales', 'basketball'],
    'Dwight' : ['beets', 'sales', 'bears', 'battlestar galactica'],
    'Michael' : ['basketball', 'sales', 'pranks'],
    'Pam' : ['pranks', 'beets', 'art'],
    'Angela': ['accounting', 'beets', 'cats']

}

"""## Get the Keys"""

list(office.keys())

"""## Get the Values"""

list(office.values())

"""## Get the Items"""

for key,value in office.items():
  print(f'Key: {key}')
  print(f'Values: {value}')

"""# Add and Delete Keys"""

office['Oscar'] = ['accounting']

del office['Oscar']

"""1. Change Jim's interests to ['pranks', 'hanging out with friends']
    


"""

office

office['Jim'] = ['pranks', 'hanging out with friends']

"""2. How many interests does Angela have?
    


"""

len(office['Angela'])

"""3. How many keys are in this dictionary?
    


"""

len(office.keys())

"""4. How many people have 'sales' as an interest?"""

office

# Using "in"
'v' in ['a' , 'b',  'c']

# 4. Which people have 'sales' as an interest?

people = []
for person, interests in office.items():
  if 'sales' in interests:
    people.append(person)

print(people)

"""# Reverse the Dictionary"""

office

office_reversed = {}

for name, interests in office.items():
  for interest in interests:
    if interest not in office_reversed.keys():
      office_reversed[interest] = [name]
    else:
      office_reversed[interest].append(name)

office_reversed

"""# The Network"""

# Keys represent the user
# Values represent all the people they are following

network = {
    
    'Shreya' : ['Aneesha', 'Tammy', 'Dora the Explorer'],
    'Aneesha' : ['Shreya', 'Tammy', 'Shawn Mendes', 'Taylor Swift'],
    'Tammy' : ['Shreya', 'Taylor Swift', 'Aneesha'],
    'Taylor Swift' : ['Shawn Mendes', 'Tammy'],
    'Shawn Mendes' : ['Taylor Swift', 'Tammy'],
    'Dora the Explorer' : ['Tammy']
    
}

"""1. Who follows the most number of people?


"""



"""2. How many people follow Tammy?


"""



"""3. Who has the most followers?"""



"""# Dataframes"""

import pandas as pd

grades = {
    
    'Shreya' : [78, 98, 87, 56, 79],
    'Aneesha' : [87, 68, 98, 90, 45],
    'Tammy' : [100, 100, 100, 99 , 98]
    
}

df = pd.DataFrame(grades, index=['calculus', 'us history', 'english', 'statistics', 'biology'])
df

df['Shreya'].describe()