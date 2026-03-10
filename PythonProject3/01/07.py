import streamlit as st

# text input
# password 인자 활용
string = st.text_input(
    'Movie title',
    placeholder='Write down the title of your favourite movie',
    type='password'
)

if string:
    st.write(f'Your answer is {string}')