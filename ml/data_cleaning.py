import pandas as pd


data = pd.read_csv('Student Mental health.csv')

#data cleaning

#change objet type to datatime
data['Timestamp'] = pd.to_datetime(data['Timestamp'])
data['month'] = data['Timestamp'].dt.month_name()
data['day'] = data['Timestamp'].dt.day_name()
data['year'] = data['Timestamp'].dt.year
data['hour'] = data['Timestamp'].dt.hour

#change null values of Age
data['Age'].fillna(data['Age'].median(), inplace = True)
data['Age'] = data['Age'].astype(int)

print(data.columns)
