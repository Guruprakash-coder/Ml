# -*- coding: utf-8 -*-
"""
Created on Tue Dec 23 23:13:27 2025

@author: gurup
"""

import pandas as pd
from sklearn.linear_model import LinearRegression

# --- Step 1: Create some dummy data ---
data = {
    'Hours_Studied': [1, 2, 3, 4, 5],
    'Exam_Score': [50, 60, 70, 80, 90]
}
df = pd.DataFrame(data)

print("Current Data:")
print(df)
print("-" * 20)

# --- Step 2: Prepare the data for the model ---
# X is the input (Features), y is the output (Target)
X = df[['Hours_Studied']]
y = df['Exam_Score']

# --- Step 3: Train the Machine Learning model ---
model = LinearRegression()
model.fit(X, y)

# --- Step 4: Make a prediction ---
# We ask: "If I study for 6 hours, what score will I get?"
prediction = model.predict([[6]])

print(f"If you study for 6 hours, the model predicts a score of: {prediction[0]}")