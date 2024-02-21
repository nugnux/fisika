import streamlit as st

x = st.slider(
    'Pilih rentang',
    0.0, 100.0, (25.0, 75.0))
st.write('nilai x:', x)
y = st.slider(
    'Set nilai',
    0.0, 100.0, 25.0)
st.write('nilai y:', y)
