import streamlit as st

option = st.multiselect(
    label='your selection is',
    options=['Car', 'Airplane', 'Train', 'Ship'],
    placeholder='Select transportation'
)
st.write(f'you selected {option}')