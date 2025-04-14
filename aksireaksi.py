import streamlit as st
import streamlit_book as stb

# Header
st.header('Aksi Reaksi :sparkles:')
st.subheader('Nugroho')
#nilai
if 'nilai' not in st.session_state:
    st.session_state['nilai'] = 0

st.write('nilai = ', st.session_state.nilai)

x = stb.single_choice("Gerak jatuh bebas merupakan salah satu contoh aksi-reaksi", ["Benar", "Salah"], 1)
st.write(x)

if (x[0]):
  if (x[1]):
    st.write("Jawaban Benar")
    st.session_state['nilai'] += 1
  else:
    y = stb.single_choice("Aksi reaksi bekerja pada satu benda", ["Benar", "Salah"], 1)

