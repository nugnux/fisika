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
st.write('I=', i,'A =',i*1000,'mA')


#Ayunan
st.header("Ayunan Bandul", divider=True)

l = st.slider('Panjang tali : ',1., 57., 1., .1)
st.write('l:', l, 'cm')
t = 2*np.pi*np.sqrt(((l+np.random.random()-0.5)/100) /9.8)
st.write('Periode ayunan:', t, 's')

#Pegas
st.header("Ayunan Pegas", divider=True)
k = st.slider('k : ',10., 5710., 70., .1)
st.write('k:', k, 'N/m')
m = st.slider('m ',1.0, 573.,1., .1)
st.write('m:', m, ' g')
tp = 2*np.pi*np.sqrt((m/1000)/(k+np.random.random()-.5))
st.write('Periode Ayunan Pegas=', tp,' s = ',1000*tp,'ms')






