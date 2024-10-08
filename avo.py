import streamlit as st

r = st.slider('R = ',1., 4700., 1., .1)
#st.write('R:', r)
v = st.slider('V ',0.0, 12., 0.)
#st.write('V:', v)
i = v/r
st.write('I:', i)
