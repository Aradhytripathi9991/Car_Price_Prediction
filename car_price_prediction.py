import pandas as pd
import numpy as np
import datetime
import xgboost as xgb
import streamlit as st

def main():
    html_temp = """<h1>Car Price Prediction</h1>"""
    model = xgb.XGBRegressor()
    model.load_model("xg_model.json")
    
    st.markdown(html_temp, unsafe_allow_html=True)
    st.markdown("This is a simple web application that predicts the price of a car based on its features. Please enter the details of the car below and click on the 'Predict' button to get the estimated price.")
    
    p1 = st.number_input("please enter the ex-showroom price(in lakhs)",2.5,25.0,step=1.0)
    
    p2 = st.number_input("please enter the car driven(in kilometers)",100,500000,step=100)
    
    s1 = st.selectbox("please select the fuel type",["Petrol","Diesel","CNG"])
    if s1 == "petrol":
        p3 = 0
    elif s1 == "diesel":
        p3 = 1
    else:
        p3 = 2
    
    s2 = st.selectbox("please select the seller type",["Dealer","Individual"])
    if s2 == "dealer":
        p4 = 0
    else:
        p4 = 1
    
    s3 = st.selectbox("please select the transmission type",["Manual","Automatic"])
    if s3 == "manual":
        p5 = 0
    else:
        p5 = 1
        
    s4 = st.selectbox("please select the owner type",["First Owner","Second Owner","Third Owner","Fourth & Above Owner"])
    if s4 == "first owner":
        p6 = 0
    elif s4 == "second owner":
        p6 = 1
    elif s4 == "third owner":
        p6 = 2
    else:
        p6 = 3
        
    s5 = st.selectbox("please select the car type",["Hatchback","Sedan","SUV","MUV","Coupe","Convertible"])
    if s5 == "hatchback":
        p7 = 0
    elif s5 == "sedan":
        p7 = 1
    elif s5 == "suv":
        p7 = 2
    elif s5 == "muv":
        p7 = 3
    elif s5 == "coupe":
        p7 = 4
    else:
        p7 = 5
        
    p8 = st.slider("how many owners has the car had?", 0, 4, 1)
    
    date_time = datetime.datetime.now()
    years = st.number_input("please enter the year of purchase",1990,date_time.year,step=1)
    p9= date_time.year - years
        
    data_new = pd.DataFrame({
       'Present_Price':p1,
       'Kms_Driven':p2,
         'Fuel_Type':p3,
         'Seller_Type':p4,
         'Transmission':p5,
         'Owner':p6
   },index=[0])
    
    if st.button("Predict"):
        prediction = model.predict(data_new)
        st.success(f"The estimated price of the car is: {prediction[0]:.2f} lakhs")
    
    
    
    
    
if __name__ == '__main__':
    main()
    
    
