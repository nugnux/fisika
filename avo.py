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

import time
import numpy as np
import pandas as pd

_LOREM_IPSUM = """
Lorem ipsum dolor sit amet, **consectetur adipiscing** elit, sed do eiusmod tempor
incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
"""


def stream_data():
    for word in _LOREM_IPSUM.split(" "):
        yield word + " "
        time.sleep(0.02)

    yield pd.DataFrame(
        np.random.randn(5, 10),
        columns=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"],
    )

    for word in _LOREM_IPSUM.split(" "):
        yield word + " "
        time.sleep(0.02)


if st.button("Stream data"):
    st.write_stream(stream_data)






