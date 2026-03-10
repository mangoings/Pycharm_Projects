import streamlit as st

activate = st.checkbox('I agree')

if activate:
    st.write('Great!')
else:
    st.write('Bye!')

toggle = st.toggle('Turn on the switch!')
if toggle:
    st.write('Switch is turned on!')
else:
    st.write('Switch is turned off!')