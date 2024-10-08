import streamlit as st
import random
import numpy as np

st.title("Alat Ukur Tak Presisi")

#AVO
st.header("Amperemeter", divider=True)

r = st.slider('R : ',1., 4700., 1., .1)
st.write('R:', r, 'Ohm')
v = st.slider('V ',0.0, 12., 0.)
st.write('V:', v, ' Volt')
i = v/(r + random.random() - .5)
st.write('I=', i,'A =',i/1000,'mA')

#Ayunan
st.header("Ayunan", divider=True)

l = st.slider('Panjang tali : ',1., 57., 1., .1)
st.write('l:', l, 'cm')
t = np.sqrt(4 * np.pi**2 * ((l+np.random.random()-.5)/1000) /9.8)
st.write('Periode ayunan:', t, 's')



