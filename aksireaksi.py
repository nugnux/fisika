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

x1 = stb.single_choice("Sebuah benda bermassa 0,8 kg digantung pada pegas vertikal dengan konstanta k = 160 N/m. Benda digetarkan dari posisi setimbang.", 
        ["0,32 s", "0,44 s", "0,56 s", "0,62 s"], 2,
                       success='Benar, $ T = 2 \pi \sqrt{\\frac{0.8}{160}} \\approx 0.56 \,s$', 
                       error='Pastikan rumus yang anda gunakan benar, jangan lupa tanda akar.')
st.write(x1)
x2 = stb.single_choice("Apa yang terjadi terhadap frekuensi osilasi jika massa benda yang digantung pada pegas ditambah?", 
        ["Frekuensi Bertambah", "Frekuensi berkurang", "Frekuensi tetap", "Frekuensi nol"], 1,
                       success='Benar, $ f = \\frac{2 \pi} \sqrt{\\frac{k}{m}} $, jika $m$ naik maka $f$ turun', 
                       error='Ingat rumus frekuensi pada pegas')

if (x1[0]):
  st.session_state.c1 = 1
  if (x1[1]):
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
st.write('Nilai Sesi = ', nil)
st.write('Nilai Kumulatif = ', st.session_state.nilai)
