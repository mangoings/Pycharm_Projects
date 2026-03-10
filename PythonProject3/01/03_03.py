import streamlit as st
import pandas as pd

df = pd.read_csv('./input/economics.csv')

# 클릭 시 if문을 실행
st.button('hide')
if st.button('view', type='primary'):
    df = pd.read_csv('./input/economics.csv')
    df