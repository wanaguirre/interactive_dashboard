# create streamlit app
# firstly go to the terminal and run "streamlit run 01_create_streamlit_app.py"

# Ctrl+S
# ReRun on the web page

# All the code and examples are here
# https://docs.streamlit.io/en/stable/api.html

# to create a more formal web page
# https://discuss.streamlit.io/t/streamlit-navbar/14936

import streamlit as st
import pandas as pd

st.title("This is Title")

st.header("This is Header")

st.subheader("This is Subheader")

st.write("hello")

name = "Juan"

st.write(name)

import plotly.express as px

df = px.data.carshare()

# write datafame

st.write("st.write(df)")
st.write(df)

st.write("st.dataframe(df)")
st.dataframe(df)

st.write("st.dataframe(df, 200, 111)")
st.dataframe(df, 200, 111)

# st.write("st.table(df)")
# st.table(df) # display to much info

st.write("st.table(df.head())")
st.table(df.head())

# plots and charts

st.bar_chart(df["peak_hour"].value_counts())

import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.hist(df["car_hours"], bins=50)

st.pyplot(fig)

# Maps

df["lat"] = df["centroid_lat"]
df["lon"] = df["centroid_lon"]
st.map(df)

# more about maps in the link above

# widgets

# checkboxs

df2 = pd.read_csv(r"D:\Step_out\0_IT_Studies\Propulsion_Academy_Gitlab\juan-aguirre\03_Visualization\day4\data\mpg.csv")
if st.checkbox("Show dataframe"):
    st.table(df2.head())



# selectBox

st.selectbox("Choose",["1", "2", "3"])


def selection(value):

    value = int(value)+5
    st.write(value)


choosen_value = st.selectbox("Chse", pd.unique(["1", "2", "3"]))
selection(choosen_value)

# option = st.selectbox(
#     "Select Peak Hour",
#     sorted(pd.unique(df["peak_hour"]))
# )

# Layout

st.sidebar.write(name)

# Columns

left, right = st.columns(2)

left.table(df.head())
right.pyplot(fig)




