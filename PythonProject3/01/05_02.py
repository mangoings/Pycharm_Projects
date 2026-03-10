import streamlit as st

option = st.radio(
    'What is your favourite movie genre',
    ["Comedy", "Drama", "Documentary"],
    captions=['Laugh out loud', 'Get the popcorn', 'Never stop learning']
)

if option:
    st.text(f'You selected {option}')