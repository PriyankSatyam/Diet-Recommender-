import streamlit as st
import pandas as pd
from diet_utils import calculate_calories, filter_foods, generate_meal_plan

# Load the dataset
df = pd.read_csv("usda_foods.csv")

# Streamlit App
st.title("Diet Recommender 🍎")

st.sidebar.header("Enter Your Details")
age = st.sidebar.number_input("Age (years)", min_value=10, max_value=100, value=25)
gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
weight = st.sidebar.number_input("Weight (kg)", min_value=30, max_value=200, value=70)
height = st.sidebar.number_input("Height (cm)", min_value=100, max_value=250, value=170)
activity = st.sidebar.selectbox(
    "Activity Level", ["Sedentary", "Light", "Moderate", "Active", "Very Active"]
)
goal = st.sidebar.selectbox("Goal", ["Weight Loss", "Maintain", "Weight Gain"])
diet = st.sidebar.selectbox(
    "Dietary Preference", ["vegan", "vegetarian", "halal", "gluten-free"]
)

# Calculate daily calories
calories_needed = calculate_calories(age, gender, weight, height, activity, goal.lower())

st.write(f"### Your Daily Calorie Target: {int(calories_needed)} kcal")

# Filter foods based on diet
filtered_df = filter_foods(df, diet)

# Generate meal plan
meal_plan = generate_meal_plan(filtered_df, calories_needed)

st.write("### Your Recommended Meal Plan")
st.dataframe(meal_plan[["Food", "Category", "Calories", "Protein", "Carbs", "Fat"]])

# Show total nutrition
total_nutrition = meal_plan[["Calories", "Protein", "Carbs", "Fat"]].sum()
st.write("### Total Nutrition for the Day")
st.write(total_nutrition)