import streamlit as st

r = st.slider('R = ', 1.0, 4700.0, 0.1)
st.write('R:', r)
v = st.slider('V ',0.0, 12, 0.1)
st.write('V:', y)
i = v/r
st.write('I:', i)
