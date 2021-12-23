# streamlit run Exercise.py

import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go

df = pd.read_csv(r"D:\Step_out\0_IT_Studies\Propulsion_Academy_Gitlab\juan-aguirre\03_Visualization\day4\data\mpg.csv")

st.title("Highway Fuel Efficiency")

button = st.checkbox("Show dataframe")
if button:
    st.table(df.head())

# df2 = df[df["year"] == 1999].reset_index(drop=True)
# st.table(df2)


def selection_yc(year, clase, r, r_mean):
    if year == "All":
        df2 = df
        pass
    else:
        df2 = df[df["year"] == int(year)].reset_index(drop=True)
    if clase == "All":
        df3 = df2
        pass
    else:
        df3 = df2[df2["class"] == str(clase)].reset_index(drop=True)

    if r == 'Matplotlib':
        fig, ax = plt.subplots(figsize=(12, 8))
        ax.scatter(df3['displ'], df3['hwy'], alpha=0.8)

        ax.set_title("Engine Size vs. Highway Fuel Mileage")
        ax.set_xlabel("displament (l)")
        ax.set_ylabel("hwy")

        if r_mean == "Yes":
            ax.scatter(df3['displ'].mean(), df3['hwy'].mean(), alpha=1, color="y")
        else:
            pass

        st.pyplot(fig)

    else:
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=df3['displ'], y=df3['hwy'], mode="markers", marker=dict(opacity=0.8)))

        if r_mean == "Yes":
            fig.add_trace(go.Scatter(x=[df3['displ'].mean()], y=[df3['hwy'].mean()], mode="markers", marker=dict(color='orange', opacity=1)))
        else:
            pass

        fig.update_layout(
            title={"text": "Engine Size vs. Highway Fuel Mileage", "font": {"size": 24}},
            xaxis={"title": {"text": "displament (l)", "font": {"size": 18}}},
            yaxis={"title": {"text": "hwy", "font": {"size": 18}}},
        )

        st.plotly_chart(fig)





years = df["year"].unique()
years = np.append(years, "All")

clas = df["class"].unique()
clas = np.append(clas, "All")


choosen_year = st.selectbox("Choose the car's year", years, index=len(years)-1)
choosen_class = st.selectbox("Choose the car's class", clas, index=len(clas)-1)

left, center, right = st.columns(3)

radius_m_p = left.radio("Way of plotting", ('Matplotlib', 'Plotly'), index=1)

radius_select_m = center.radio("Show class mean", ('Yes', 'No'), index=1)

radius_select = right.radio("Show class meanings", ('Yes', 'No'), index=1)

selection_yc(choosen_year, choosen_class, radius_m_p, radius_select_m)

if radius_select == 'Yes':
    st.sidebar.write('''
    - Compact: Compact car is a vehicle size class — predominantly used in North America — that sits between subcompact cars and mid-size cars. The present-day definition is equivalent to the European C-segment or the British term "small family car".
    
    - Midsize: Mid-size—also known as intermediate—is a vehicle size class which originated in the United States and is used for cars that are larger than compact cars, but smaller than full-size cars.[1] The equivalent European category is D-segment, which is also called "large family car".
    
    - SUV: A sport utility vehicle or SUV is a car classification that combines elements of road-going passenger cars with features from off-road vehicles, such as raised ground clearance and four-wheel drive. There is no commonly agreed-upon definition of an SUV, and usage of the term varies between countries.
    
    - 2 Seater: IT is a vehicle with two seats, usually one for the driver and one for a passenger.
    
    - Minivan: Minivan (sometimes called simply as van) is a North American car classification for vehicles designed to transport passengers in the rear seating row(s), with reconfigurable seats in two or three rows. 
    
    - Pickup: A pickup truck or pickup is a light-duty truck that has an enclosed cabin and an open cargo area with low sides and tailgate.[1] In Australia and New Zealand, both pickups and coupé utilities are called utes, short for utility vehicle. In South Africa, people of all language groups use the term bakkie, a diminutive of bak, Afrikaans for "bowl" or "container".
    
    - Subcompact: Subcompact car is an American classification for cars which is broadly equivalent to the B-segment (Europe) or supermini (Great Britain) classifications, and smaller than a compact car.
    ''')
else:
    pass

