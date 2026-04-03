# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 14:46:08 2026

@author: gurup
"""

import pandas as pd
s=pd.Series([10,20,30,40,50])

print(s.dtype)

s.name="calories"
print(s.values)
print(s[0:3])
print(s.iloc[3])
print(s.iloc[[1,3,4]])
index=["apple","banana","grapes","oranges","mango"]
s.index=index
print(s)
print(s[0]+s['apple'])
print(s['apple':'banana'])
print(s.loc[['grapes','apple']])



 