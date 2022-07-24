import streamlit as st
st.write("""
## Streamlit App Implementation and Deployment using Heroku
### App: Subtraction - Subtract Second number from First number
""")
#Get Input

st.header('User Inputs:')

def user_input_features():
    
    first = st.number_input("First Number")
    second = st.number_input("Second Number")
    answer = first - second

    return answer

answer = user_input_features()


st.header('Answer:')
st.subheader(answer)
