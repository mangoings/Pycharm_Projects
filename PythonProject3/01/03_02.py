import streamlit as st

# 클릭 시 if문을 실행
st.button('Reset', type='primary')
if st.button('activate'):
    st.write('button activated')