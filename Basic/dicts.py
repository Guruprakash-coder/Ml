# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 15:37:51 2026

@author: gurup
"""
import pandas as pd
fruit_protein={
    "Avacado":2.0,
    "Guava": 2.6,
    "Blackberries": 2.0,
    "Oranges": 0.9,
    "Banana": 1.1,
    "Apples": 0.3,
    "Kiwi": 1.1,
    "Pomegranate": 1.7,
    "Mango": 0.8,
    "Cherries": 1.0
    }
s=pd.Series(fruit_protein,name='protein')
print(s>1)
print(s[s>1])

print(s[(s>0.5) & (s<2.0)])
s["mango"]=1.8
print(s)
