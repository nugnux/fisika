import streamlit as st

r = st.slider('R = ',min_value=1.0, max_value=4700.0, value=1., step=0.1)
st.write('R:', r)
v = st.slider('V ',0.0, 12, 0.1)
st.write('V:', y)
i = v/r
st.write('I:', i)
