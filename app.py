
import streamlit as st
import joblib
import numpy as np
from sklearn.preprocessing import StandardScaler
import pandas as pd
import warnings 

warnings.filterwarnings('ignore')

# Load the trained model and scaler
#model = joblib.load('notebooks/model.pkl')
#scaler = joblib.load('notebooks/scaler.pkl')  # Load the scaler used during training

# Load the trained model and scaler
model = joblib.load('model/gradient-model.pkl')
scaler = joblib.load('model/gradient-scaler.pkl')  # Load the scaler used during training

# Streamlit app interface
def main():
    st.title("DED Severity Prediction App")

    # Input fields from the user
    gender = st.selectbox("Gender", ["Male", "Female"])
    age = st.slider("Age", 12, 30)
    device_types = st.selectbox("Device Types Used", 
                               ['Gaming Console, Smartphone, Tablet', 
                                'Smartphone, Computer', 
                                'Tablet, Smartphone'])
    
    usage_hours = st.slider("Average Daily Usage Hours", 2, 10 )
    years_usage = st.slider("Years of Digital Device Usage", 1, 12)
    osdi_score = st.number_input("OSDI Total Score (0 - 100)", format="%.6f")
    schirmer_left = st.selectbox("Schirmer Test Left Eye", [0, 1, 2, 3, 4, 5, 10, 11, 12, 13, 14, 15] )
    schirmer_right = st.selectbox("Schirmer Test Right Eye", [0, 1, 2, 3, 4, 5, 10, 11, 12, 13, 14, 15])
    tbut_left = st.selectbox("TBUT Test Left Eye", [0, 1, 2, 3, 4, 5, 10, 11, 12, 13, 14, 15] )
    tbut_right = st.selectbox("TBUT Test Right Eye", [0, 1, 2, 3, 4, 5, 10, 11, 12, 13, 14, 15] )
    ocular_left = st.selectbox("Ocular Surface Staining Left Eye", [0, 1, 2, 3])
    ocular_right = st.selectbox("Ocular Surface Staining Right Eye", [0, 1, 2, 3])

    

    # Convert gender to numerical value for prediction
    gender_map = {"Male": 0, "Female": 1}
    gender_input = gender_map[gender]

 
    # Convert device types to numerical values (one-hot encoding or similar)
    device_map = {
        'Gaming Console, Smartphone, Tablet' : 0,
         'Smartphone, Computer' : 1,
         'Tablet, Smartphone' : 2
    }
    
    device_input = device_map[device_types]


    input_features = np.array([gender_input, age,
                          device_input ,  # 3 elements from device input
                          usage_hours, years_usage, osdi_score, 
                          schirmer_left, schirmer_right, 
                          tbut_left, tbut_right, 
                          ocular_left, ocular_right])  # 12 elements in total
    input_features = input_features.reshape(1, -1)
    
    # Make prediction on button click
    if st.button("Predict Ded Severity"):
        try:
            # Apply the same scaling that was used during training
            input_data_scaled = scaler.transform(input_features)  # Use transform to apply scaling

            # Predict with the model
            prediction = model.predict(input_data_scaled)

            predicted_severity = prediction[0]
            st.write(f"Predicted Ded Severity: {predicted_severity}")
        
        except Exception as e:
            st.error(f"Error during prediction: {e}")

# Run the Streamlit app
if __name__ == "__main__":
    main()
