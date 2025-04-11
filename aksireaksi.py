import streamlit as st
import streamlit_book as stb

# Header
st.header('Aksi Reaksi :sparkles:')
st.subheader('Nugroho')


x = stb.single_choice("Gerak jatuh bebas merupakan salah satu contoh aksi-reaksi",
                  ["Benar", "Salah"], 1)

print(x)  

if (x[1]):
  st.write("Jawaban Benar")
#else:
#  y = stb.single_choice("Aksi reaksi bekerja pada satu benda",
#                  ["Benar", "Salah"], 1)

