# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 12:03:02 2020

@author: Aneesha
"""

i_get_booleans = True

if i_get_booleans == True:
    # Only downside to single quotes -> grammar
    # Use \' if you want to include an apostrophe in your string
    print('Let\'s learn about conditonals!')
else:
    print("Let's review booleans")
    
    
    
def do_i_get_booleans(i_get_booleans):
    if i_get_booleans == True:
        print('Let\'s learn about conditonals!')
    else:
        print("Let's review booleans")
        
do_i_get_booleans(True)
do_i_get_booleans(False)
    




def my_grade(grade):

    if grade >= 90:
        print('yay! u got an A')
    elif grade >= 80:
        print('it\'s a B!')
    elif grade >= 70:
        print('You passed with a C')
    elif grade >= 60:
        print('Atleast you didn\'t fail?')
    else:
        print('retake the class.')

my_grade(80)
my_grade(70)
my_grade(75)
my_grade(92)
    


    
    
