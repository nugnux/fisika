import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# Header
st.header('Temperature Conversion :sparkles:')
st.subheader('.')

c1, c2 = st.columns(2)
with c1:
    x = st.number_input('Temperature: ',value=100)
    st.write('Convert into:')
with c2:
    sX = st.selectbox(
        'scale: ',('C', 'F', 'R','K'),
        label_visibility="visible", key='sx'
        )

    sY = st.selectbox(
        'scale: ',('C', 'F', 'R','K'),
        label_visibility="collapsed", key='sy'
        )
    
if (sX=='C'):
    if(sY=='C'):
        y = x 
    elif(sY=='F'):
        y = x * 9/5 +32
    elif(sY=='R'):
        y = x * 4/5
    elif(sY=='K'):
        y = x + 273
st.write(f"{x} {sX} = {y} {sY}")


col1, col2 = st.columns(2)
with col1:
    st.caption('.')
    

with col2:
    st.caption('.')
   
st.caption('Copyright © Nugroho Adi Pramono 2023')
