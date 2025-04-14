import streamlit as st
import streamlit_book as stb

# Header
st.header('Aksi Reaksi :sparkles:')
st.subheader('Nugroho')
#nilai
if 'nilai' not in st.session_state:
    st.session_state['nilai'] = 0
for i in range (3):
    if 's'+str(i)  not in st.session_state:
        st.session_state['s'+str(i)] = 0

x = stb.single_choice("Gerak jatuh bebas merupakan salah satu contoh aksi-reaksi", 
                      ["Benar", "Salah"], 1)
st.write(x)

if (x[0]):
  if (x[1]):
    st.write("Jawaban Benar")
    st.session_state['nilai'] += 1
    st.session_state.s1 = 1
    
if (!st.session_state.s1):
    y = stb.single_choice("Aksi reaksi bekerja pada satu benda", ["Benar", "Salah"], 1)

st.write('Nilai = ', st.session_state.nilai)
