import streamlit as st
import pickle
import numpy as np

model = pickle.load(open(r'C:\Users\praty\Dropbox\PC\Desktop\Code\Rent_pred\rent_predictor.pkl', 'rb'))

st.title("Rent Predictor")

type = st.number_input("NO of BHK")
bathroom = st.number_input("NO of Bathrooms")
total_floor = st.number_input("NO of Floors in building")

latitude = st.number_input("latitude")
longitude = st.number_input("longitude")
property_size = st.number_input("Property Size")

# Use selectbox for the following features
st.write("Press 1 for yes and 0 for no")

lift = st.selectbox("Is there a lift?", [0, 1])
swimming_pool = st.selectbox("Is there a Swimming Pool?", [0, 1])
INTERNET = st.selectbox("Is there INTERNET?", [0, 1])
AC = st.selectbox("Is there AC?", [0, 1])
INTERCOM = st.selectbox("Is there an INTERCOM?", [0, 1])
SECURITY = st.selectbox("Is there SECURITY?", [0, 1])


water_supply = st.selectbox(
    'What kind of Water do you get?\n0 for BOREWELL \n1 for CORPORATION \n2 for CORP_BORE',
    (0, 1, 2))

furnishing = st.selectbox(
    'Is your house furnished?\n0 for Fully furnished \n1 for Not Furnished \n2 for Semi Furnished',
    (0, 1, 2))

parking = st.selectbox(
    'Car parking?\n1 for Four wheeler \n3 for Two wheeler \n2 for None \n0 for Both',
    (0, 1, 2))

facing = st.selectbox(
    'What kind of Water do you get?\n0 for East \n1 for North \n2 for North East \n3 for North West \n4 for South \n5 for South East \n6 for South west \n7 for West',
    (0, 1, 2, 3, 4, 5, 6, 7))

# Create a Predict button
if st.button("Predict"):
    features = np.array([
        [type, latitude, longitude, lift, swimming_pool, furnishing, parking, property_size,
         bathroom, facing, total_floor, water_supply, INTERNET, AC, INTERCOM, SECURITY]
    ])
    
    # Make prediction using your model
    prediction = model.predict(features)

    # Display the predicted rent value
    st.write("Predicted Rent:", prediction[0])
