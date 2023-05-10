import streamlit as st 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
from data_cleaning import data
from palettes.palettes import *


# Set the page background color to white
sns.set_style(style='darkgrid')

st.set_option('deprecation.showPyplotGlobalUse', False)
st.title('Student Mental Health Exploratory Data Analysis')
st.subheader('What is the point of this project?')
st.write('Mental health among university students is a critical issue that can impact their ability to succeed academically and personally. In this project, an exploratory data analysis (EDA) was conducted to better understand the prevalence of three of the most common mental health disorders among university students: depression, anxiety, and panic attacks. Through a variety of data visualization techniques, the relationship between these disorders and factors such as gender, age, and academic level were explored. The goal of this project is to provide valuable insights into the patterns and trends in mental health among university students, in order to improve understanding and attention to these critical health challenges')




#data visualization

#normalize the years distribution
data['Year'] = data['Your current year of Study'].str.extract(r'(\d+)').astype(int)
year_counts = data.groupby('Year').size()



#anxiety group
def ap():
    #gender distribution
    gender_freq = data['Choose your gender'].value_counts()

    #anxiety distribution and frequency
    anxiety_group = data.groupby(['Choose your gender', 'Do you have Anxiety?','Year']).size().reset_index(name='counter')
    sns.barplot(x="Year", y="counter", hue="Do you have Anxiety?", data=anxiety_group.query("`Choose your gender` == 'Female'"), palette=sea, saturation=0.5)

    # Config grafic
    plt.title("Anxiety in females students", fontsize = 13)
    plt.xlabel("Year")
    plt.ylabel("Person number")
    st.pyplot()

    sns.barplot(x="Year", y="counter", hue="Do you have Anxiety?", data=anxiety_group.query("`Choose your gender` == 'Male'"), palette=summer, saturation=0.5)
    plt.title("Anxiety in male students", fontsize = 13)
    plt.xlabel("Year")
    plt.ylabel("Person number")
    st.pyplot()

#depression groups
def dp():
    #depression group
    Depression_group = data.groupby(['Year', 'Choose your gender', 'Do you have Depression?']).size().reset_index(name='counter')

    #Female depresion
    sns.barplot(x='Year', y='counter', hue='Do you have Depression?', palette=halloween, saturation=0.5, data=Depression_group.query("`Choose your gender` == 'Female'"))
    plt.title("Depression tendecies in female students")
    plt.xlabel("Year")
    plt.ylabel("Person number")
    st.pyplot()


    #Male depression
    sns.barplot(x='Year', y = 'counter', hue = 'Do you have Depression?', palette = halloween2,saturation=0.5, data=Depression_group.query("`Choose your gender` == 'Male'") )
    plt.title("Depression tendecies in male students")
    plt.xlabel("Year")
    plt.ylabel("Person number")
    st.pyplot()

#panic attack groups
def pap():
    #Panic attack group
    panic_group = data.groupby(['Year', 'Choose your gender', 'Do you have Panic attack?']).size().reset_index(name='counter')

    #Female Panic
    sns.barplot(x='Year', y='counter', hue='Do you have Panic attack?', palette=cold, saturation=0.7, data = panic_group.query("`Choose your gender` == 'Female'"))
    plt.title("Panic Attacks in females students")
    plt.xlabel("Year")
    plt.ylabel("Person number")
    st.pyplot()

    #Male panic
    sns.barplot(x='Year', y='counter', hue='Do you have Panic attack?', palette=cold2, saturation=0.7, data=panic_group.query("`Choose your gender` == 'Male'"))
    plt.xlabel('Year')
    plt.ylabel('Person number')
    plt.title('Panic Attacks in male students')


    st.pyplot()


def tp():
    treatment_group = data.groupby(['Year','Choose your gender', 'Do you seek'])


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
    st.title("Gender and Age")
    st.write("""
    As we can see in the following graph, the majority of students who responded to this small survey were mostly female, with a proportionally small amount of male students, we can also see the ages of these students.
    """)

    sns.displot(data, x="Age", hue="Choose your gender", multiple="stack", palette=cold, kind="kde")
    plt.xlabel('Age')
    plt.title('Gender distribution')

    st.pyplot() # show grafic on the streamlit screen




if show_anxiety:
    st.title("Anxiety tendencies between university students")
    st.write("""
    Anxiety is one of the most serious yet common problems that we see when talking about mental health. Thanks to data visualization we can see the trends of anxiety among male and female students.
    """)
    st.write("""
    As we can see in the following graph, although there are more female students, we can see that those who suffer from anxiety are less than half, with a significant decrease from year to year, until the last one where there is almost no anxiety.
    """)
    st.write("""
    On the part of the male students, we can notice that there is a higher rate of anxiety, with the first and second year students suffering the most anxiety, although in the last years it suddenly decreases and ceases to exist.
    """)
    ap()
    

if show_depression:
    st.title("Depression tendences in students")
    st.write("""
    When talking about mental illnesses, the most common without any doubt is depression, being sadly a mental illness which affects young adults a lot, reaching the point of threatening their own life and lowering their average.
    """)
    st.write("""
    Thanks to the graph, we can notice that women have a higher rate of depression than men, with high peaks in the first and third year, but male students have very low rates, with the highest rate in the second year, and then disappear completely.
    """)
    dp()

if show_panic:
    st.title("Panic attacks in university students")
    st.write("""It is common for students' mental health to be affected by the stress and pressure associated with their academic and personal responsibilities. In general, it has been observed that women experience higher rates of anxiety disorders, such as panic attacks, compared to men. This may be due to a combination of biological, psychological and social factors.
                As for the difference between freshmen and seniors in terms of panic attacks, it could be the result of several factors. It is possible that freshmen are experiencing a higher level of stress due to the transition to college life, while seniors may have developed better stress and anxiety management skills over time.
                It is also possible that fourth-year students have learned to avoid situations that trigger their panic attacks or have sought treatment for their anxiety, which may explain why they have a lower incidence of panic attacks compared to first-year students.
                """)
    pap()



