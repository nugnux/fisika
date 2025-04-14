import streamlit as st
import streamlit_book as stb

# Header
st.header('Aksi Reaksi :sparkles:')
st.subheader('Nugroho')
nilai = 0

x = stb.single_choice("Gerak jatuh bebas merupakan salah satu contoh aksi-reaksi", ["Benar", "Salah"], 1)
st.write(x)

if (x[0]):
  if (x[1]):
    st.write("Jawaban Benar")
    nilai += 1
  else:
    y = stb.single_choice("Aksi reaksi bekerja pada satu benda", ["Benar", "Salah"], 1)

st.write(nilai)

