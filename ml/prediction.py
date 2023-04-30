from data_pre import encoded_data
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# cargar el dataset
df = encoded_data

# seleccionar columnas objetivo y características
objetivo_cols = ['Do you have Anxiety?_Yes', 'Do you have Depression?_Yes', 'Do you have Panic attack?_Yes']
caract_cols = [col for col in df.columns if col not in objetivo_cols]

# separar datos en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(df[caract_cols], df[objetivo_cols], test_size=0.2, random_state=42)

# escalar los datos de entrenamiento y prueba
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# crear y entrenar modelo de regresión logística
model = LogisticRegression()
model.fit(X_train, y_train)

# hacer predicciones sobre los datos de prueba
y_pred = model.predict(X_test)

# calcular precisión del modelo
accuracy = accuracy_score(y_test, y_pred)
print("Precisión en el conjunto de entrenamiento:", accuracy)
