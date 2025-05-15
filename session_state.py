import streamlit as st

#Why when we append anthor element the precedent was removed --> because the program strated in beign

if "text_list" not in st.session_state:
    st.session_state.text_list = []

user_input = st.text_input("Entrer some text")

if st.button('Append'):
    st.session_state.text_list.append(user_input)

if st.button("Clear"):
    st.session_state.text_list = []

st.write("Text List :" , st.session_state.text_list)
st.write("session state" ,  st.session_state)