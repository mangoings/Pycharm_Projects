import streamlit as st

from datetime import time

start_time, end_time = st.slider(
    'Working time is...',
    min_value=time(0), max_value=time(23),
    value=(time(8), time(18)),
    format='HH:mm'
)
st.text(f'Working time: {start_time}, {end_time}')