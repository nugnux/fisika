import streamlit as st
import numpy as np
import matplotlib as plt

x = st.slider('Pilih rentang', 0.0, 2.0, (.2, .5))
st.write('nilai x:', x)
y = st.slider('Set nilai',0.0, 100.0, 25.0)
st.write('nilai y:', y)

t = np.linspace(x[0],x[1],100)
u = np.sin(t)
