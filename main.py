import streamlit as st 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
import streamlit as st


# Set the page background color to white



data = pd.read_csv('Student Mental health.csv')
st.set_option('deprecation.showPyplotGlobalUse', False)
sns.set_style(style='darkgrid')
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

st.title('Student Mental Health Exploratory Data Analysis')

#data visualization


#normalize the years distribution
data['Year'] = data['Your current year of Study'].str.extract(r'(\d+)').astype(int)
year_counts = data.groupby('Year').size()



#anxiety group
def ap():
    #gender distribution
    gender_freq = data['Choose your gender'].value_counts()

    #anxiety distribution and frequency
    anxiety_group = data.groupby(['Choose your gender', 'Do you have Anxiety?']).size().reset_index(name='counter')
    sns.barplot(x="Choose your gender", y="counter", hue="Do you have Anxiety?", data=anxiety_group, palette="Greens")

    # Config grafic
    plt.title("Anxiety Counter")
    plt.xlabel("Gender")
    plt.ylabel("Person number")

    return(st.pyplot())

#depression groups
def dp():
    #depression group
    Depression_group = data.groupby(['Year', 'Choose your gender', 'Do you have Depression?']).size().reset_index(name='counter')

    #Female depresion
    g_female = sns.catplot(x='Year', y='counter', hue='Do you have Depression?', palette='Blues', kind='bar', row='Choose your gender', data=Depression_group.query("`Choose your gender` == 'Female'"))
    g_female.set_axis_labels()
    g_female.set_titles("Female")
    st.pyplot()

    #Male depression
    g_male = sns.catplot(x='Year', y='counter', hue='Do you have Depression?', palette='rocket', kind='bar', row='Choose your gender', data=Depression_group.query("`Choose your gender` == 'Male'"))
    g_male.set_axis_labels()
    g_male.set_titles("Male")
    st.pyplot()

#panic attack groups
def pap():
    #Panic attack group
    panic_group = data.groupby(['Year', 'Choose your gender', 'Do you have Panic attack?']).size().reset_index(name='counter')

    #Female Panic
    p_female = sns.catplot(x='Year', y='counter', hue='Do you have Panic attack?', palette='Blues', kind='bar', row='Choose your gender', data = panic_group.query("`Choose your gender` == 'Female'"))
    p_female.set_axis_labels()
    p_female.set_titles("Female")
    st.pyplot()

    #Male panic
    p_male = sns.catplot(x='Year', y='counter', hue= 'Do you have Panic attack?', palette = 'rocket', kind = 'bar', row = 'Choose your gender', data= panic_group.query("`Choose your gender` == 'Male'"))
    p_male.set_axis_labels()
    p_male.set_titles("Male")
    st.pyplot()


show_dataframe = st.sidebar.checkbox("show dataset📜")
show_genders = st.sidebar.checkbox("Show gender distribution")
show_anxiety = st.sidebar.checkbox("Show student anxiety information")
show_depression = st.sidebar.checkbox('Show student depression information')
show_panic = st.sidebar.checkbox('Show student panic attack information')

# Si el usuario selecciona la casilla de ver el dataframe, muestra el dataframe
if show_dataframe:
    st.write("Link of the oficial dataset: https://www.kaggle.com/datasets/shariful07/student-mental-health")
    st.dataframe(data)#age distribution and frequency 

if show_genders:
    st.write("This is the student gender distribution by gender and age")
    sns.displot(data, x="Age", hue="Choose your gender", multiple="stack", palette="rocket", kind="kde")
    plt.xlabel('Age')
    plt.ylabel('Frequency')
    plt.title('Age distribution')

    st.pyplot() # show grafic on the streamlit screen


if show_anxiety:
    st.write("In this graphic we can see anxiety tendencies about the students")
    ap()
    

if show_depression:
    st.write("In this graphic we can see depressed students tendecies")
    dp()

if show_panic:
    st.write("In this graphic we can see panic students tendecies")
    pap()

