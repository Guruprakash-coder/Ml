# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 16:01:33 2026

@author: gurup
"""

import numpy as np
import pandas as pd
ser =pd.Series(['a',np.nan,1,np.nan,2])
data = {
"Name": ["Alice", "Bob", "Charlie", "David", "Eve", "Alice"],
"Age": [25, 30, 35, np.nan, 29, 25],
"Department": ["HR", "IT", "Finance", "IT", "HR", "HR"],
"Salary": [50000, 60000, 70000, 62000, np.nan, 50000]
}
df = pd.DataFrame(data)
print(df)
print(df.iloc[1:3])
print(df.loc[1:3,["Age","Department"]])