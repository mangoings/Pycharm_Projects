import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# 이미지 표현
from PIL import Image

img = Image.open('./input/image1.jpg')
st.image(img, width=300, caption='Image from Unsplash')