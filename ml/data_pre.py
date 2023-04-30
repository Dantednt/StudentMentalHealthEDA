import pandas as pd
import numpy as np
from data_cleaning import data



df = data[['Choose your gender', 'What is your course?', 'What is your CGPA?', 'Marital status', 'Do you have Depression?',
            'Do you have Anxiety?', 'Do you have Panic attack?', 'Did you seek any specialist for a treatment?','Your current year of Study']]

cat_vars = ['Choose your gender', 'What is your course?', 'What is your CGPA?', 'Marital status', 'Do you have Depression?',
            'Do you have Anxiety?', 'Do you have Panic attack?', 'Did you seek any specialist for a treatment?', 'Your current year of Study']

encoded_data = pd.get_dummies(df, columns=cat_vars)
encoded_data.to_csv("ready.csv", index=False)
print(encoded_data.columns)