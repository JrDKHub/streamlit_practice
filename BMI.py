import streamlit as st

st.title('BMI CALCULATOR')

w = st.number_input('Weight',help='in kg')
h = st.number_input('height',help='in m')


def calc_bmi(w,h):
    return (w/(h*h))

if st.button('Calculate BMI'):
    bmi = calc_bmi(w,h)
    if(bmi < 18.5):
        st.warning("You are Underweight")
    elif(bmi >= 18.5 and bmi < 25):
        st.success("Normal build")
    elif(bmi >= 25 and bmi < 30):
        st.warning("Overweight")
    elif(bmi >= 30 and bmi < 35):
        st.error("Moderate OBESITY  ")
    elif(bmi >= 35 and bmi < 40):
        st.error("Severe OBESITY")
    elif(bmi >= 40):
        st.error("MORBID OBESITY")
