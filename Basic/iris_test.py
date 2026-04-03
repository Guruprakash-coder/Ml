import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix

# --- 1. Load Data (The Textbook) ---
iris = load_iris()
X = iris.data
y = iris.target
class_names = iris.target_names  # ['setosa', 'versicolor', 'virginica']

# --- 2. Split Data (Separate Study vs Exam questions) ---
# 80% for training, 20% for testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# --- 3. Train Model (The Study Session) ---
model = GaussianNB()
model.fit(X_train, y_train)

# --- 4. Predict (The Exam) ---
y_pred = model.predict(X_test)

# --- 5. Check Accuracy (The Grade) ---
acc = accuracy_score(y_test, y_pred)
print(f"Accuracy: {acc*100:.2f}%")

# --- 6. VISUALIZATION (The Report Card) ---
# Calculate the Confusion Matrix
cm = confusion_matrix(y_test, y_pred)

# Plot it using Seaborn
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=class_names,
            yticklabels=class_names)
plt.xlabel('Predicted Label')
plt.ylabel('Actual Label')
plt.title('Confusion Matrix: Where did the model make mistakes?')
plt.show()