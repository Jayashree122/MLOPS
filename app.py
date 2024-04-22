import streamlit as st
import pickle
import numpy as np

# Load the saved Linear Regression model
with open('gdp.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Function to predict GDP per capita using the loaded model
def predict_passengers(Age,Tonnage,length,cabins,passenger_density,crew):
    features = np.array([Age,Tonnage,length,cabins,passenger_density,crew])
    features = features.reshape(1,-1)
    passengers = model.predict(features)
    return passengers[0]

# Streamlit UI
st.title('PASSENGERS PREDICTION')
st.write("""   
Enter the values for the input features to predict passengers.
""")

# Input fields for user
Age = st.number_input('Age')
Tonnage = st.number_input('Tonnage')
length = st.number_input('length')
cabins = st.number_input('cabins')
passenger_density= st.number_input('passenger_density')
crew = st.number_input('crew')

# Prediction button
if st.button('Predict'):
    # Predict Sport
    passengers_prediction = predict_passengers(Age,Tonnage,length,cabins,passenger_density,crew)
    st.write(f"Predicted passengers: {passengers_prediction}")