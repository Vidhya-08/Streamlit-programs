import streamlit as st
import pandas as pd

st.header("BUTTON")

if(st.button('Say Hello')):
    st.write("Hey hello friend!")
else:
    st.write("Goodbye")

st.header("DOWNLOAD BUTTON")
sample_text="This text will be downloaded"
st.download_button("Download text",sample_text)

with open("photo.jpeg","rb") as file:
    btn=st.download_button(
        label="Download image",
        data=file,
        file_name="photo.jpeg",
        mime="image/jpeg"
        )
        
'''
@st.cache

def convert_df(df):
    return df.to_csv().encode('utf-8')
df1=pd.read_csv("address.csv")
csv=convert_df(df1)
st.download_button(label="Download data as csv",
                   data=csv,
                   file_name="large_df.csv",
                   mime="text/csv")
'''

st.title("CHECKBOX")
agree=st.checkbox("I agree")
if agree:
    st.write("Great!!")


st.title("RADIOBUTTON")
colour=st.radio(
    "What's your favourite colour?",
    ("Red","Blue","Pink","Black"))

if colour=='Blue':
    st.write("You selected Blue")
else:
    st.write("You selected",colour)


st.title("SELECTBOX")
option=st.selectbox(
    "Which foods you like the most",
    ('Biriyani','Chicken fried rice','Noodles'))

st.write("You like",option)


st.title("Slider")
from datetime import time,datetime

age=st.slider('How old are you?',0,100,25)
st.write("I am",age,"years old")
values=st.slider(
    "Select a range of values",
    0.0,100.0,(25.0,75.0))
st.write("Vlaues:",values)
appointment=st.slider(
    "Schedule your appointment:",
    value=(time(11,30),time(12,45)))
st.write("You're scheduled for:",appointment)
start_time=st.slider(
    'When do you start?',
    value=datetime(2023,1,1,9,30),
    format="MM/DD/YY-hh:mm")
st.write("Start time:",start_time)


st.title("Text Input")
title=st.text_input('Movie Title','Life of Brian')
st.write("The movie title is :",title)


st.title("Number input")
num=st.number_input("Insert a number")
st.write("The number is :",num)


st.title("Date Input")
d=st.date_input(
    'When is your birthday?',
    datetime(2003,8,21))
st.write("Your Birthday is on :",d)
                    





















    


















































    



















