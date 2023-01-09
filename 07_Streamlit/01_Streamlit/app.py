# > pip install streamlit 
# > streamlit run app.py 
# > streamlit run app.py --server.port 9999

import os 
from pathlib import Path 
import pickle 
import pandas as pd 

import streamlit as st

os.chdir(Path(__file__).parent)






def load_model():

    with open("./models/model_linear_reg_v1.pkl", mode = "rb") as file:
        model = pickle.load(file)

    return model



def main():
    model = load_model() 

    # Write a title
    st.title("Welcome by Area Prediction Application")

    # Add Input Field
    area = int(st.text_input("Area", 50))


    if st.button("Predict"):
        predicted_price = round(float(model.predict([[area]])), 2)

        st.success(f"The predicted price for the area {area} is: {predicted_price}")


if __name__ == "__main__":
    main()