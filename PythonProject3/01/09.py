import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

df = sns.load_dataset('tips')

fig, ax = plt.subplots()
sns.histplot(df, x='total_bill', ax=ax, hue='time')

# streamlit 대시보드에 표현
st.pyplot(fig)