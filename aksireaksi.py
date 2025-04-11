import streamlit as st
import streamlit_book as stb

# Header
st.header('Aksi Reaksi :sparkles:')
st.subheader('Nugroho')


stb.single_choice("Gerak jatuh bebas merupakan salah satu contoh aksi-reaksi",
                  ["Benar", "Salah"], 1)
