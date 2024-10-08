import streamlit as st

r = st.slider('R = ', -7.0, 7.0, (.2, .5))
st.write('R:', r)
v = st.slider('V ',0.0, 12, .1)
st.write('V:', y)
i = v/r
st.write('I:', i)
