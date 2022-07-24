import streamlit as st
st.write("""
# Subtraction
Subtract Second number from First number
""")
#Get Input

st.header('User Input Parameters')

def user_input_features():
    
    first = st.number_input("First_Number")
    second = st.number_input("Second_Number")
    answer = first - second

    return answer

answer = user_input_features()


st.subheader('Answer')
st.write(answer)
