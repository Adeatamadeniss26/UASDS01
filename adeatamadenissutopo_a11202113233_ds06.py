# -*- coding: utf-8 -*-
"""AdeatamaDenisSutopo_A11202113233_DS06

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1rmFpryDRHm2xl8ZOf5G9HfezWFogfgji
"""

#1.Pengumpulan Data
import pandas as pd # Import the pandas library and assign it to the alias 'pd'

file_path = '/content/drive/MyDrive/UASDS01/water_potability.csv'
water_data = pd.read_csv(file_path)
water_data.head()



#2.Menelaah Data
import pandas as pd

file_path = '/content/drive/MyDrive/UASDS01/water_potability.csv'
water_data = pd.read_csv(file_path)

# Select the desired columns
selected_columns = ['ph', 'Hardness', 'Solids', 'Chloramines', 'Sulfate', 'Conductivity',
                   'Organic_carbon', 'Trihalomethanes', 'Turbidity', 'Potability']
selected_data = water_data[selected_columns]

# Display information about the dataset
print("Number of rows:", len(selected_data))
print("\nData types of each column:\n", selected_data.dtypes)
print("\nUnique values in each column:")
for column in selected_columns:
    print(f"{column}: {selected_data[column].unique()[:20]}") # Displaying first 20 unique values for brevity
    if len(selected_data[column].unique()) > 20:
        print(f"   ... ({len(selected_data[column].unique())} unique values in total)")

#3.Validasi dan Visualisasi Data
!pip install matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the data
file_path = '/content/drive/MyDrive/UASDS01/water_potability.csv'
water_data = pd.read_csv(file_path)

# Select the desired columns
selected_columns = ['ph', 'Hardness', 'Solids', 'Chloramines', 'Sulfate', 'Conductivity',
                   'Organic_carbon', 'Trihalomethanes', 'Turbidity', 'Potability']
selected_data = water_data[selected_columns]

# 1. Check and Impute Missing Values and Outliers

# Function to handle missing values and outliers
def handle_missing_outliers(data, column):
    # Calculate mean and standard deviation
    mean = data[column].mean()
    std = data[column].std()

    # Replace missing values with mean
    data[column] = data[column].fillna(mean)

    # Replace outliers with mean (using 3 standard deviations as threshold)
    upper_bound = mean + 3 * std
    lower_bound = mean - 3 * std
    data[column] = np.where((data[column] > upper_bound) | (data[column] < lower_bound), mean, data[column])

    return data

# Apply the function to each selected column
for column in selected_columns[:-1]:  # Exclude 'Potability' as it's categorical
    selected_data = handle_missing_outliers(selected_data, column)

# 2. Visualize Data Distribution

# Function to create bar plots
def plot_distribution(data, column, title):
    plt.figure(figsize=(8, 6))
    data[column].plot(kind='hist', bins=20, edgecolor='black')
    plt.title(title)
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.show()


# Plot distributions before and after handling missing values and outliers
for column in selected_columns[:-1]:
    plot_distribution(water_data[selected_columns], column, f'{column} Distribution (Before)')
    plot_distribution(selected_data, column, f'{column} Distribution (After)')

#4. Menentukan Objek Data
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Load the data
file_path = '/content/drive/MyDrive/UASDS01/water_potability.csv'
water_data = pd.read_csv(file_path)

# Select features and target
features = ['ph', 'Hardness', 'Solids', 'Chloramines', 'Sulfate', 'Conductivity',
            'Organic_carbon', 'Trihalomethanes', 'Turbidity']
target = 'Potability'
X = water_data[features]
y = water_data[target]

# Handle missing values (if any) - replace with mean
X = X.fillna(X.mean())

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Feature scaling (Standardization)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Create and train the model (Logistic Regression)
model = LogisticRegression(random_state=42)
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")
print(classification_report(y_test, y_pred))

#5.Membersihkan Data
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Load the data
file_path = '/content/drive/MyDrive/UASDS01/water_potability.csv'
water_data = pd.read_csv(file_path)

# Select features and target
features = ['ph', 'Hardness', 'Solids', 'Chloramines', 'Sulfate', 'Conductivity',
            'Organic_carbon', 'Trihalomethanes', 'Turbidity']
target = 'Potability'
X = water_data[features]
y = water_data[target]

# 1. Correlation Heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(X.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap of Water Quality Features')
plt.show()

# 2. Distribution Histogram Plots
X.hist(bins=20, figsize=(12, 10), edgecolor='black')
plt.suptitle('Distribution Histogram Plots of Water Quality Features', y=1.02)
plt.tight_layout()
plt.show()

# Handle missing values (if any) - replace with mean
X = X.fillna(X.mean())

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Feature scaling (Standardization)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Create and train the model (Logistic Regression)
model = LogisticRegression(random_state=42)
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")
print(classification_report(y_test, y_pred))

#6.Konstruksi Data
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Load the data
file_path = '/content/drive/MyDrive/UASDS01/water_potability.csv'
water_data = pd.read_csv(file_path)

# Select features and target
features = ['ph', 'Hardness', 'Solids', 'Chloramines', 'Sulfate', 'Conductivity',
            'Organic_carbon', 'Trihalomethanes', 'Turbidity']
target = 'Potability'
X = water_data[features]
y = water_data[target]

# 1. Correlation Heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(X.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap of Water Quality Features')
plt.show()

# 2. Distribution Histogram Plots
X.hist(bins=20, figsize=(12, 10), edgecolor='black')
plt.suptitle('Distribution Histogram Plots of Water Quality Features', y=1.02)
plt.tight_layout()
plt.show()

# Handle missing values (if any) - replace with mean
X = X.fillna(X.mean())

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Feature scaling (Standardization)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Create and train the model (Logistic Regression)
model = LogisticRegression(random_state=42)
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")
print(classification_report(y_test, y_pred))

#7.Pemodelan
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Load the data
file_path = '/content/drive/MyDrive/UASDS01/water_potability.csv'
water_data = pd.read_csv(file_path)

# Select features and target
features = ['ph', 'Hardness', 'Solids', 'Chloramines', 'Sulfate', 'Conductivity',
            'Organic_carbon', 'Trihalomethanes', 'Turbidity']
target = 'Potability'
X = water_data[features]
y = water_data[target]

# Handle missing values (if any) - replace with mean
X = X.fillna(X.mean())

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Feature scaling (Standardization)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 1. Logistic Regression
lr_model = LogisticRegression(random_state=42)
lr_model.fit(X_train, y_train)
lr_pred = lr_model.predict(X_test)
lr_accuracy = accuracy_score(y_test, lr_pred)
print("Logistic Regression Accuracy:", lr_accuracy)
print(classification_report(y_test, lr_pred))

# Confusion Matrix for Logistic Regression
lr_cm = confusion_matrix(y_test, lr_pred)
sns.heatmap(lr_cm, annot=True, fmt="d", cmap="Blues")
plt.title("Confusion Matrix - Logistic Regression")
plt.xlabel("Predicted Label")
plt.ylabel("True Label")
plt.show()

# 2. Decision Tree
dt_model = DecisionTreeClassifier(random_state=42)
dt_model.fit(X_train, y_train)
dt_pred = dt_model.predict(X_test)
dt_accuracy = accuracy_score(y_test, dt_pred)
print("Decision Tree Accuracy:", dt_accuracy)
print(classification_report(y_test, dt_pred))

# Confusion Matrix for Decision Tree
dt_cm = confusion_matrix(y_test, dt_pred)
sns.heatmap(dt_cm, annot=True, fmt="d", cmap="Blues")
plt.title("Confusion Matrix - Decision Tree")
plt.xlabel("Predicted Label")
plt.ylabel("True Label")
plt.show()

# 3. K-Nearest Neighbors
knn_model = KNeighborsClassifier(n_neighbors=5)  # You can adjust n_neighbors
knn_model.fit(X_train, y_train)
knn_pred = knn_model.predict(X_test)
knn_accuracy = accuracy_score(y_test, knn_pred)
print("K-Nearest Neighbors Accuracy:", knn_accuracy)
print(classification_report(y_test, knn_pred))

# Confusion Matrix for K-Nearest Neighbors
knn_cm = confusion_matrix(y_test, knn_pred)
sns.heatmap(knn_cm, annot=True, fmt="d", cmap="Blues")
plt.title("Confusion Matrix - K-Nearest Neighbors")
plt.xlabel("Predicted Label")
plt.ylabel("True Label")
plt.show()

#8.Evaluasi
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Load the data
file_path = '/content/drive/MyDrive/UASDS01/water_potability.csv'
water_data = pd.read_csv(file_path)

# Select features and target
features = ['ph', 'Hardness', 'Solids', 'Chloramines', 'Sulfate', 'Conductivity',
            'Organic_carbon', 'Trihalomethanes', 'Turbidity']
target = 'Potability'
X = water_data[features]
y = water_data[target]

# Handle missing values (if any) - replace with mean
X = X.fillna(X.mean())

# 1. Model Evaluation before Normalization
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train models
models = {
    "Logistic Regression": LogisticRegression(random_state=42),
    "Decision Tree": DecisionTreeClassifier(random_state=42),
    "K-Nearest Neighbors": KNeighborsClassifier(n_neighbors=5)
}

for model_name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"{model_name} Accuracy (Before Normalization): {accuracy}")


# 2. Model Evaluation after Normalization
# Feature scaling (Standardization)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Create and train models
models = {
    "Logistic Regression": LogisticRegression(random_state=42),
    "Decision Tree": DecisionTreeClassifier(random_state=42),
    "K-Nearest Neighbors": KNeighborsClassifier(n_neighbors=5)
}

for model_name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"{model_name} Accuracy (After Normalization): {accuracy}")

!python -m http.server 80

#9. Kesimpulan
!pip install scikit-learn
!pip install streamlit

import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from pyngrok import ngrok  # Import pyngrok

# Load your trained model (replace with your model loading logic)
# Example:
import pickle
with open('/content/drive/MyDrive/UASDS01/model.pkl', 'rb') as file:
    model = pickle.load(file)

st.title("Water Potability Prediction")

# Get user input
ph = st.number_input("Enter pH value:")
hardness = st.number_input("Enter Hardness value:")
# ... (get input for other features) ...

# Create a DataFrame for prediction
input_data = pd.DataFrame({
    'ph': [ph],
    'Hardness': [hardness],
    # ... (other features) ...
})

# Make prediction
prediction = lr_model.predict(input_data)

# Display prediction
if prediction[0] == 1:
    st.write("The water is predicted to be potable.")
else:
    st.write("The water is predicted to be not potable.")
    # Model selection
model_choice = st.selectbox("Select Model:", ["Logistic Regression", "Decision Tree", "K-Nearest Neighbors"])

# Prediction logic (choose model based on user selection)
if model_choice == "Logistic Regression":
    prediction = lr_model.predict(input_data)
elif model_choice == "Decision Tree":
    prediction = dt_model.predict(input_data)
else:
    prediction = knn_model.predict(input_data)

"""Berdasarkan analisis perbandingan algoritma Logistic Regression, Decision Tree, dan K-Nearest Neighbors untuk prediksi potability air, dapat disimpulkan sebagai berikut:

Tingkat Akurasi:

Logistic Regression: Akurasi sekitar 60-62%.
Decision Tree: Akurasi sekitar 57-60%.
K-Nearest Neighbors: Akurasi sekitar 58-61%.
Sederhana dan mudah diinterpretasi: Model Logistic Regression mudah dipahami dan dijelaskan, sehingga memudahkan dalam analisis dan pengambilan keputusan.
Relatif cepat: Proses pelatihan dan prediksi dengan Logistic Regression relatif cepat, sehingga cocok untuk dataset yang besar.
Performa cukup baik: Meskipun akurasinya tidak sempurna, Logistic Regression tetap memberikan performa yang cukup baik dalam memprediksi potability air.
"""