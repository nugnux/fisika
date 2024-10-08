import streamlit as st
import random

st.title("Alat Ukur Tak Presisi")
st.title("_Streamlit_ is :blue[cool] :sunglasses: ")

r = st.slider('R = ',1., 4700., 1., .1)
#st.write('R:', r)
v = st.slider('V ',0.0, 12., 0.)
#st.write('V:', v)
i = v/(r + random.random() - .5)
st.write('I:', i)

