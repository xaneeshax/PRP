# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 13:20:27 2020

@author: Aneesha
"""



def buy_balloons(dollars):
    if dollars >= 9:
        print('you can buy all of them!')
    elif dollars >= 7:
        print('blue and green balloons')
    elif dollars >= 2:
        print('i can get the red balloon')
    else:
        print('no balloons')
        
buy_balloons(2)
buy_balloons(5)
buy_balloons(8)
buy_balloons(10)