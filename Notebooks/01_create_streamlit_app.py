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
import plotly.express as px
from urllib.request import urlopen
import json
import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go

st.title("US unemployment rate")


with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/fips-unemp-16.csv",
                   dtype={"fips": str})


fig = px.choropleth_mapbox(df, geojson=counties, locations='fips', color='unemp',
                           color_continuous_scale="Viridis",
                           range_color=(0, 12),
                           mapbox_style="carto-positron",
                           zoom=3, center = {"lat": 37.0902, "lon": -95.7129},
                           opacity=0.5,
                           labels={'unemp':'unemployment rate'}
                          )
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

st.plotly_chart(fig)



