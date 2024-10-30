import streamlit as st
import pandas as pd
import numpy as np

# Page Title
st.title("Health Data Input Form")

# Section for Categorical Data
st.header("Select Your Information")

# Dropdown for 'State'
state = st.selectbox("State", 
    ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado',
     'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia',
     'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky',
     'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota',
     'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire',
     'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota',
     'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina',
     'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia',
     'Washington', 'West Virginia', 'Wisconsin', 'Wyoming', 'Guam', 'Puerto Rico',
     'Virgin Islands'])

# Dropdown for 'Sex'
sex = st.selectbox("Sex", ['Female', 'Male'])

# Dropdown for 'GeneralHealth'
general_health = st.selectbox("General Health", ['Very good', 'Excellent', 'Fair', 'Poor', 'Good'])

# Dropdown for 'LastCheckupTime'
last_checkup_time = st.selectbox("Last Checkup Time", [
    'Within past year (anytime less than 12 months ago)',
    'Within past 2 years (1 year but less than 2 years ago)',
    'Within past 5 years (2 years but less than 5 years ago)',
    '5 or more years ago'])

# Section for Yes/No Medical History
st.header("Medical History")

# Yes/No Selectors for Medical History
col1, col2 = st.columns(2)

with col1:
    had_heart_attack = st.radio("Had Heart Attack?", ['No', 'Yes'])
    had_stroke = st.radio("Had Stroke?", ['No', 'Yes'])
    had_asthma = st.radio("Had Asthma?", ['No', 'Yes'])
    had_skin_cancer = st.radio("Had Skin Cancer?", ['No', 'Yes'])

with col2:
    had_copd = st.radio("Had COPD?", ['No', 'Yes'])
    had_depressive_disorder = st.radio("Had Depressive Disorder?", ['No', 'Yes'])
    had_kidney_disease = st.radio("Had Kidney Disease?", ['No', 'Yes'])
    had_arthritis = st.radio("Had Arthritis?", ['No', 'Yes'])


# Section for Physical and Lifestyle Data
st.header("Physical and Lifestyle Information")

# Dropdowns for lifestyle choices and disabilities
smoker_status = st.selectbox("Smoker Status", [
    'Never smoked', 'Current smoker - now smokes some days', 'Former smoker',
    'Current smoker - now smokes every day'])

e_cigarette_usage = st.selectbox("E-Cigarette Usage", [
    'Not at all (right now)', 'Never used e-cigarettes in my entire life',
    'Use them every day', 'Use them some days'])

# Yes/No options for other lifestyle or health checks
chest_scan = st.radio("Had a Chest Scan?", ['No', 'Yes'])
flu_vax_last_12 = st.radio("Received Flu Vaccine in Last 12 Months?", ['No', 'Yes'])
pneumo_vax_ever = st.radio("Ever Had Pneumonia Vaccine?", ['No', 'Yes'])

# User Inputs for Numeric Data
st.header("Enter Your Health Metrics")

# Numeric input for 'PhysicalHealthDays'
physical_health_days = st.number_input("Physical Health Days (last 30 days)", min_value=0, max_value=30, value=0)

# Numeric input for 'MentalHealthDays'
mental_health_days = st.number_input("Mental Health Days (last 30 days)", min_value=0, max_value=30, value=0)

# Numeric input for 'SleepHours'
sleep_hours = st.number_input("Average Sleep Hours per Night", min_value=0.0, max_value=24.0, value=7.0)

# Numeric input for 'HeightInMeters'
height_in_meters = st.number_input("Height in Meters", min_value=0.0, max_value=3.0, value=1.75)

# Numeric input for 'WeightInKilograms'
weight_in_kilograms = st.number_input("Weight in Kilograms", min_value=0.0, max_value=300.0, value=70.0)

st.markdown("---")  # Horizontal line for separation

# Submit button
if st.button("Submit"):
    # Store inputs in a DataFrame or dictionary
    user_data = {
        'State': state,
        'Sex': sex,
        'GeneralHealth': general_health,
        'LastCheckupTime': last_checkup_time,
        'HadHeartAttack': had_heart_attack,
        'HadStroke': had_stroke,
        'HadAsthma': had_asthma,
        'HadSkinCancer': had_skin_cancer,
        'HadCOPD': had_copd,
        'HadDepressiveDisorder': had_depressive_disorder,
        'HadKidneyDisease': had_kidney_disease,
        'HadArthritis': had_arthritis,
        'SmokerStatus': smoker_status,
        'ECigaretteUsage': e_cigarette_usage,
        'ChestScan': chest_scan,
        'FluVaxLast12': flu_vax_last_12,
        'PneumoVaxEver': pneumo_vax_ever,
        'PhysicalHealthDays': physical_health_days,
        'MentalHealthDays': mental_health_days,
        'SleepHours': sleep_hours,
        'HeightInMeters': height_in_meters,
        'WeightInKilograms': weight_in_kilograms,
    }
    
    # Display user input
    st.write("Your Input:")
    st.json(user_data)

    # Optionally, add data to a DataFrame
    df = pd.DataFrame([user_data])
    st.write(df)
