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
    st.experimental_set_query_params(s_nilai = nilai)
  else:
    y = stb.single_choice("Aksi reaksi bekerja pada satu benda", ["Benar", "Salah"], 1)
app_state = st.experimental_get_query_params()  
st.write(app_state)
f "s_nilai" in app_state:
    nnilai = app_state["s_nilai"][0]
    st.write("Here is your result", nilai)
else:
    st.write("No result to display, compute a value first.")
st.write(nilai)

