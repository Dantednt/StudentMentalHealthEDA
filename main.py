import streamlit as st 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
import streamlit as st
from ml.data_cleaning import data
from PIL import Image

# Set the page background color to white
sns.set_style(style='darkgrid')

st.set_option('deprecation.showPyplotGlobalUse', False)
st.title('Student Mental Health Exploratory Data Analysis')
st.subheader('What is the point of this project?')
st.write('Mental health among university students is a critical issue that can impact their ability to succeed academically and personally. In this project, an exploratory data analysis (EDA) was conducted to better understand the prevalence of three of the most common mental health disorders among university students: depression, anxiety, and panic attacks. Through a variety of data visualization techniques, the relationship between these disorders and factors such as gender, age, and academic level were explored. The goal of this project is to provide valuable insights into the patterns and trends in mental health among university students, in order to improve understanding and attention to these critical health challenges')
github_url = "https://github.com/Dantednt"
github_image_url = "https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png"

html_code = f"<a href='{github_url}' target='_blank'><img src='{github_image_url}' height='40'></a>"

st.sidebar.write(html_code, unsafe_allow_html=True)



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
    p_female = sns.catplot(x='Year', y='counter', hue='Do you have Panic attack?', palette=([(1.0, 0.4, 0.4), (0.8, 0.2, 0.2)]), kind='bar', row='Choose your gender', data = panic_group.query("`Choose your gender` == 'Female'"))
    p_female.set_axis_labels()
    p_female.set_titles("Female")
    st.pyplot()

    #Male panic
    sns.displot(data=panic_group.query("`Choose your gender` == 'Male'"), x="Year", hue="Do you have Panic attack?", multiple="stack", palette = sns.color_palette([(1.0, 0.4, 0.4), (0.8, 0.2, 0.2)]),kind="kde")
    plt.xlabel('Year')
    plt.ylabel('Density')
    plt.title('Panic Attack by Year (Male)')

    st.pyplot()


st.sidebar.title("data visualization")
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
    st.write("""It is common for students' mental health to be affected by the stress and pressure associated with their academic and personal responsibilities. In general, it has been observed that women experience higher rates of anxiety disorders, such as panic attacks, compared to men. This may be due to a combination of biological, psychological and social factors.
                As for the difference between freshmen and seniors in terms of panic attacks, it could be the result of several factors. It is possible that freshmen are experiencing a higher level of stress due to the transition to college life, while seniors may have developed better stress and anxiety management skills over time.
                It is also possible that fourth-year students have learned to avoid situations that trigger their panic attacks or have sought treatment for their anxiety, which may explain why they have a lower incidence of panic attacks compared to first-year students.
                """)
    pap()


