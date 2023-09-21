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
elif (sX=='F'):
    if(sY=='C'):
        y = (x-32) * 5/9
    elif(sY=='F'):
        y = x 
    elif(sY=='R'):
        y = (x-32) * 4/9
    elif(sY=='K'):
        y = (x-32) * 5/9 + 273
elif (sX=='R'):
    if(sY=='C'):
        y = x * 5/4 
    elif(sY=='F'):
        y = x * 9/4 +32
    elif(sY=='R'):
        y = x 
    elif(sY=='K'):
        y = x * 5/4 + 273
elif (sX=='K'):
    if(sY=='C'):
        y = x - 273
    elif(sY=='F'):
        y = (x-273) * 9/5 +32
    elif(sY=='R'):
        y = (x-273) * 4/5
    elif(sY=='K'):
        y = x

st.divider()
st.write(f"{x} {sX} = {y} {sY}")
st.divider()

col1, col2 = st.columns(2)
with col1:
    st.caption('.')
    

with col2:
    st.caption('.')
   
st.caption('Copyright © Nugroho Adi Pramono 2023')
