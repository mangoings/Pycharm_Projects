import streamlit as st


# button
def button_write():
    st.write('button activated')


st.button('Reset', type='primary')
st.button('activate', on_click=button_write)