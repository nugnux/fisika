import streamlit as st
import random
import numpy as np



st.title("Alat Ukur Tak Presisi")


#AVO
st.header("Amperemeter", divider=True)
avo =  st.container(border=True)
with avo:
  r = st.slider('R : ',1., 4700., 1., .1)
  st.write('R:', r, 'Ohm')
  v = st.slider('V ',0.0, 12., 0.)
  st.write('V:', v, ' Volt')
  i = v/(r + random.random() - .5)
  st.write('I =', i,'A =',i*1000,'mA')


#Ayunan
st.header("Ayunan Bandul", divider=True)
ayunan = st.container(border=True)
with ayunan:
  l = st.slider('Panjang tali : ',1., 57., 1., .1)
  st.write('l:', l, 'cm')
  t = 2*np.pi*np.sqrt(((l+np.random.random()-0.5)/100) /9.8)
  st.write('Periode ayunan =', t, 's')

#KPegas
st.header("Pegas", divider=True)
kpegas = st.container(border=True)
with kpegas:
  kp = st.slider('Konstanta Pegas : ',10., 5710., 7., .1)
  st.write('k:', kp, 'N/m')
  f = st.slider('Gaya tarik : ',0., 5710., 0., .1)
  st.write('k:', f, 'N/m')
  dx = (f+np.random.random()-0.5)/kp
  st.write('$\delta x$ =', dx, 'm =',dx*100,'cm')


#Pegas
st.header("Ayunan Pegas", divider=True)
pegas = st.container(border=True)
with pegas:
  k = st.slider('k : ',10., 5710., 70., .1)
  st.write('k:', k, 'N/m')
  m = st.slider('m ',1.0, 573.,1., .1)
  st.write('m:', m, ' g')
  tp = 2*np.pi*np.sqrt((m/1000)/(k+np.random.random()-.5))
  st.write('Periode Ayunan Pegas =', tp,' s = ',1000*tp,'ms')






