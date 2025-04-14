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
for i in range (3):
    if 'c'+str(i)  not in st.session_state:
        st.session_state['c'+str(i)] = 0

x1 = stb.single_choice("Gerak jatuh bebas merupakan salah satu contoh aksi-reaksi", 
                      ["Benar", "Salah"], 1)
st.write(x1)

if (x[0]):
  st.session_state.c1 = 1
  if (x[1]):
    st.write("Jawaban Benar")
    st.session_state['nilai'] += 1
    st.session_state.s1 = 1
  else:
    st.session_state.s1 = 0

    
if (st.session_state.s1 == 0 and st.session_state.c1 == 1 ):
    y1 = stb.single_choice("Aksi reaksi bekerja pada satu benda", ["Benar", "Salah"], 1)
    if (y1[0]):
      st.session_state.c1 = 1
      if (y1[1]):
        st.write("Jawaban Benar")
        st.session_state['nilai'] += 1
        st.session_state.s1 = .5
      else:
        st.session_state.s1 = 0

nil = 0
for i in range(3):
    nil += st.session_state['s'+str(i)]
st.write('Nilai Total= ', nil)
st.write('Nilai Total= ', st.session_state.nilai)
