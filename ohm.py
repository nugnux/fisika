import streamlit as st
import random
import numpy as np

st.title("Alat Ukur Tak Presisi - Hukum Ohm")

#AVO
st.header("Amperemeter", divider=True)
avo =  st.container(border=True)
with avo:
  v = st.slider('V ',0.0, 12., 0.)
  st.write('V:', v, ' Volt')
  i = (v + random.random() - .5)/(371)
  st.write('I =', i,'A =',i*1000,'mA')


st.header("Ayunan Bandul", divider=True)
