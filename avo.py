import streamlit as st
import random

st.title("Alat Ukur Tak Presisi")
st.header("Amperemeter", divider=True)

r = st.slider('R : ',1., 4700., 1., .1)
st.write('R:', r, 'Ohm')
v = st.slider('V ',0.0, 12., 0.)
#st.write('V:', v, ' Volt')
i = v/(r + random.random() - .5)
st.write('I=', i,'A =',i/1000,'mA')

st.header("Ayunan", divider=True)


