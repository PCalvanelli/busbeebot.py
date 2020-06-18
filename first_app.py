import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
import altair as alt
import time
import matplotlib.pyplot as plt
from PIL import Image

#header and version title
st.write('v',1.0)
st.title('Busbee Bot :palm_tree: :v:')

#Shitball Avatar

image = Image.open('img/john.jpg')
st.image(image, caption="Hello! I am your new data analyst, Shitball Higgins!", width=200)

#Upload CSV File
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

#Upload CSV File through widget
#Add spinner to simulate shitball Higgins reading data
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    with st.spinner(text='Please hold. Shitball Higgins is attempting to read your data...'):
        time.sleep(1)
    st.write(df)
    st.success('Shitball Higgins :hankey: successfully loaded your file!')

#Select specific variables for data analysis
#Pulls columns data as variables

if st.button("Describe Data"):
    with st.spinner(text='Please hold. Shitball Higgins :hankey: is looking intensly at your data...'):
        time.sleep(3)
    st.write(df.describe().T)
    st.success("Shitball Higgins found some gems :gem:!")

'''

---

'''

#Plot and Visualize
st.header("Sample Visualization :bar_chart:")
st.write("Now that you have selected that variables you'd like to explore, let's look at one way this can be visualized.")
if st.button("Show Plot"):
    st.area_chart(df)
