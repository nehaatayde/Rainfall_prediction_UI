import streamlit as st
import numpy as np
import pickle
import datetime

# Load trained Random Forest model
model_filename = "RF_rainfall_model.pkl"  # Ensure the file is uploaded
with open(model_filename, "rb") as file:
    rf_model = pickle.load(file)

# Streamlit UI
def main():
    st.title("Monthly Rainfall Prediction")
    st.write("Enter weather parameters and select a month to predict rainfall amount.")
    
    # Month selection
    current_year = datetime.datetime.now().year
    month_options = [datetime.date(current_year, i, 1).strftime('%B') for i in range(1, 13)]
    selected_month = st.selectbox("Select a Month for Prediction", month_options)
    
    # Input fields (top 11 correlated features)
    mean_sunshine = st.number_input("Mean Sunshine (hours)")
    mean_vapour_pressure = st.number_input("Mean Vapour Pressure (hPa)")
    dew_point = st.number_input("Dew Point (°C)")
    atmospheric_pressure = st.number_input("Atmospheric Pressure (hPa)")
    mean_sea_level = st.number_input("Mean Sea Level Pressure (hPa)")
    min_temp = st.number_input("Min Temperature (°C)")
    max_temp = st.number_input("Max Temperature (°C)")
    relative_humidity = st.number_input("Relative Humidity (%)")
    wind_speed = st.number_input("Wind Speed (km/h)")
    solar_radiation = st.number_input("Solar Radiation (MJ/m²)")
    evapotranspiration = st.number_input("Evapotranspiration (mm)")
    
    # Future prediction logic (example: incorporating month as a feature, if applicable in the model)
    month_index = month_options.index(selected_month) + 1  # Convert month to numerical value
    
    # Prediction button
    if st.button("Predict Rainfall"):
        input_data = np.array([[mean_sunshine, mean_vapour_pressure, dew_point,
                                atmospheric_pressure, mean_sea_level, min_temp,
                                max_temp, relative_humidity, wind_speed,
                                solar_radiation, evapotranspiration, month_index]])
        prediction = rf_model.predict(input_data)
        st.success(f"Predicted Rainfall for {selected_month}: {prediction[0]:.2f} mm")

if __name__ == "__main__":
    main()
