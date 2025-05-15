# bmi_calculator.py

import streamlit as st

def calculate_bmi(weight, height):
    if height == 0:
        return 0
    return round(weight / (height ** 2), 2)

def main():
    st.title("🧮 BMI Calculator")
    st.write("Calculate your Body Mass Index (BMI)")

    # Input fields
    weight = st.number_input("Enter your weight (kg)", min_value=1.0, step=0.1)
    height = st.number_input("Enter your height (m)", min_value=0.1, step=0.01)

    if st.button("Calculate BMI"):
        bmi = calculate_bmi(weight, height)
        st.success(f"Your BMI is: {bmi}")

        # Show health message based on BMI
        if bmi < 18.5:
            st.warning("You are underweight.")
        elif 18.5 <= bmi < 24.9:
            st.info("You have a normal weight.")
        elif 25 <= bmi < 29.9:
            st.warning("You are overweight.")
        else:
            st.error("You are obese.")

if __name__ == "__main__":
    main()
