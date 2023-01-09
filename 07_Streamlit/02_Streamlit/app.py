# > pip install streamlit 
# > streamlit run app.py 
# > streamlit run app.py --server.port 9999
# Emopjis : https://www.webfx.com/tools/emoji-cheat-sheet/


import os 
from pathlib import Path 
import pickle 
import pandas as pd 

import streamlit as st

os.chdir(Path(__file__).parent)



@st.cache
def get_data_frame():
    df = pd.read_csv("./multireg.csv")
    return df 





# Get the whole datasource
df = get_data_frame()


############################################
# Side Bar
############################################
st.sidebar.header("Filter the data")

area = st.sidebar.multiselect (
    "Select the area:",
    options = df["area"].unique(),
    default = df["area"].unique(),
)

room_count = st.sidebar.multiselect (
    "Select the Room Count:",
    options = df["roomcount"].unique(),
    default = df["roomcount"].unique(),
)


df_selected = df.query("area == @area & roomcount == @room_count")


############################################
# Web Page
############################################

st.title(":chart_with_upwards_trend: Area price Dashboard")

st.markdown("## Information")

# Aggregation Values
total_area = df_selected["area"].sum()
avg_price = round(df_selected["price"].mean(), 2)
message = "Very good price"


# Split the area of the page into 3x columns
left_col, middle_col, right_col = st.columns(3)

with left_col:
    st.subheader("Total area:")
    st.subheader(f"{total_area} m2")

with middle_col:
    st.subheader("Average Price:")
    st.subheader(f"{avg_price} €")

with right_col:
    st.subheader("Message:")
    st.subheader(f"{message}")


############################################
# Show the dataframe
############################################

st.markdown("---")

st.markdown("## :file_folder: Data Table")
st.dataframe(df_selected)



############################################
# Remove Hamburger ICON using CSS
############################################

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """



st.markdown(hide_st_style, unsafe_allow_html = True)