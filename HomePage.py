import streamlit as st
import pandas as pd 
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
from io import StringIO

st.set_page_config(page_title="Heart Health Status", layout="wide")
st.title("Welcome to Heart Health Status ❤️")

# Load data
df = pd.read_csv('HEALTH_HEART_2022_reduced.csv')

st.write("Original DataFrame:")
st.dataframe(df)

# Define columns of interest globally
chronic_conditions = ['HadHeartAttack', 'HadAngina', 'HadStroke', 'HadAsthma', 'HadSkinCancer', 
                      'HadCOPD', 'HadDepressiveDisorder', 'HadKidneyDisease', 'HadArthritis', 'HadDiabetes']

# Tabs for different sections
tab1, tab2, tab3 = st.tabs(['🏠 Welcome', '🔧 Handling Data & Feature Extraction', '📊 Data Understanding'])

# Tab 1: Overview of Data
with tab1:
    st.header('Welcome to Health Heart Status ❤️🧪', help='In this page, we will explore and understand the columns in the data frame.')
    st.write("First, we will display the columns to understand each feature.")
    st.code(df.columns.tolist())

    st.info('Check the data types with `df.info()` for a better understanding of each column.')
    st.code('df.info()')
    
    buffer = StringIO()
    df.info(buf=buffer)
    s = buffer.getvalue()
    st.write("### DataFrame Info:")
    st.text(s)

    st.info('Some numeric columns are in float format due to NaNs.')

# Functions for feature extraction
def calculate_bmi(row):
    """Calculates BMI from height and weight."""
    return row['WeightInKilograms'] / row['HeightInMeters'] ** 2 if not pd.isna(row['WeightInKilograms']) and not pd.isna(row['HeightInMeters']) else np.nan

def extract_chronic_condition(row):
    """Determines if a chronic condition exists."""
    return 'HadChronicCondition' if any(row[cond] == 'Yes' for cond in chronic_conditions) else 'NoChronicCondition'

def calculate_health_score(row):
    """Calculates a health score based on multiple conditions."""
    score = 50  # Base score

    # GeneralHealth scoring
    health_scoring = {'Excellent': 10, 'Very good': 7, 'Good': 5, 'Fair': -5, 'Poor': -10}
    score += health_scoring.get(row['GeneralHealth'], 0)

    # PhysicalHealthDays scoring
    score += 10 if row['PhysicalHealthDays'] <= 5 else 5 if row['PhysicalHealthDays'] <= 10 else -7 if row['PhysicalHealthDays'] <= 20 else -10 if row['PhysicalHealthDays'] > 20 else 0
    
    # MentalHealthDays scoring
    score += 10 if row['MentalHealthDays'] <= 5 else 5 if row['MentalHealthDays'] <= 10 else -7 if row['MentalHealthDays'] <= 20 else -10 if row['MentalHealthDays'] > 20 else 0

    # BMI scoring
    if 18.5 <= row['BMI'] <= 24.9:
        score += 10
    elif 25 <= row['BMI'] <= 29.9:
        score += 5
    elif 30 <= row['BMI'] <= 39.9:
        score -= 7
    elif row['BMI'] >= 40 or row['BMI'] < 18.5:
        score -= 10

    # SleepHours scoring
    score += 10 if 6 <= row['SleepHours'] <= 9 else 5 if row['SleepHours'] <= 12 else -7 if row['SleepHours'] <= 24 else -10

    # SmokerStatus scoring
    smoker_scoring = {
        'Never smoked': 10,
        'Former smoker': 7,
        'Current smoker - now smokes some days': -7,
        'Current smoker - now smokes every day': -10
    }
    score += smoker_scoring.get(row['SmokerStatus'], 0)

    # ECigaretteUsage scoring
    ecig_scoring = {
        'Never used e-cigarettes in my entire life': 10,
        'Not at all (right now)': 5,
        'Use them some days': -7,
        'Use them every day': -10
    }
    score += ecig_scoring.get(row['ECigaretteUsage'], 0)

    # AlcoholDrinkers scoring
    score += 10 if row['AlcoholDrinkers'] == 'No' else -10 if row['AlcoholDrinkers'] == 'Yes' else 0

    return max(0, min(score, 100))

# Tab 2: Feature Extraction
with tab2:
    st.subheader('Handling Data & Feature Extraction')
    st.write("Extracted Features: BMI, HealthScore, ChronicConditions")
    
    # Apply feature extraction functions
    df['BMI'] = df.apply(calculate_bmi, axis=1)
    df['ChronicCondition'] = df.apply(extract_chronic_condition, axis=1)
    df['HealthScore'] = df.apply(calculate_health_score, axis=1)
    
    st.write("New Columns added:")
    st.dataframe(df[['BMI', 'ChronicCondition', 'HealthScore']])

# Tab 3: Data Understanding
with tab3:
    st.header('Understanding the Data 🔍')
    
    st.write("Descriptive Statistics of Numerical Columns:")
    st.code(df.describe())
    
    categorical_columns = list(df.select_dtypes(include='object').columns)
    selected_column = st.selectbox(label='Select a Categorical Column to Analyze', options=categorical_columns)
    
    if selected_column:
        st.write(f"Unique Values in '{selected_column}':", df[selected_column].unique())
        st.write(f"Value Counts for '{selected_column}':")
        st.write(df[selected_column].value_counts())
        

# Sidebar settings
st.sidebar.header("Settings")
st.sidebar.text("Adjust your preferences here!")
