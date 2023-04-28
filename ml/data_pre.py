import pandas as pd
import numpy as np
from data_cleaning import data



df = data[['Choose your gender', 'What is your course?', 'What is your CGPA?', 'Marital status', 'Do you have Depression?',
            'Do you have Anxiety?', 'Do you have Panic attack?', 'Did you seek any specialist for a treatment?']]

cat_vars = ['Choose your gender', 'What is your course?', 'What is your CGPA?', 'Marital status', 'Do you have Depression?',
            'Do you have Anxiety?', 'Do you have Panic attack?', 'Did you seek any specialist for a treatment?']

encoded_data = pd.get_dummies(df, columns=cat_vars)

print(encoded_data.head(5))