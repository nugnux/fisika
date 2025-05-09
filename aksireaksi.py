import streamlit as st
import streamlit_book as stb

# Header
st.header('Aksi Reaksi :sparkles:')
st.subheader('Nugroho')
#nilai
if 'nilai' not in st.session_state:
    st.session_state['nilai'] = 0
for i in range (4):
    if 's'+str(i)  not in st.session_state:
        st.session_state['s'+str(i)] = 0
for i in range (3):
    if 'c'+str(i)  not in st.session_state:
        st.session_state['c'+str(i)] = 0

x1 = stb.single_choice("Sebuah benda bermassa 0,8 kg digantung pada pegas vertikal dengan konstanta k = 160 N/m. Benda digetarkan dari posisi setimbang. Berapakah periode osilasi benda tersebut?", 
        ["0,32 s", "0,44 s", "0,56 s", "0,62 s"], 2,
                       success='Benar, $ T = 2 \pi \sqrt{\\frac{0.8}{160}} \\approx 0.56 \,s$', 
                       error='Pastikan rumus yang anda gunakan benar, jangan lupa tanda akar.')
st.write(x1)
x2 = stb.single_choice("Apa yang terjadi terhadap frekuensi osilasi jika massa benda yang digantung pada pegas ditambah?", 
        ["Frekuensi Bertambah", "Frekuensi berkurang", "Frekuensi tetap", "Frekuensi nol"], 1,
                       success='Benar, $ f = \\frac{1}{2 \pi} \sqrt{\\frac{k}{m}} $, jika $m$ naik maka $f$ turun', 
                       error='Ingat rumus frekuensi pada pegas')

x3 = stb.single_choice("Pernyataan manakah yang benar mengenai energi dalam gerak harmonis sederhana pada sistem pegas?", 
        ["Energi kinetik selalu lebih besar dari energi potensial", 
         "Energi mekanik total berubah-ubah selama osilasi", 
         "Energi mekanik total tetap, tetapi bentuknya berubah antara kinetik dan potensial", 
         "Energi potensial pegas tidak bergantung pada posisi benda"], 
                       2,
                       success='Benar! Energi terus-menerus berubah bentuk, tapi jumlah totalnya tetap.', 
                       error='Salah. Ingat rumus kekekalan energi')


if (x1[0]):
  st.session_state.c1 = 1
  if (x1[1]):
    st.session_state['nilai'] += 1
    st.session_state.s1 = 1
  else:
    st.session_state.s1 = 0
if (x2[0]):
  st.session_state.c2 = 1
  if (x2[1]):
    st.session_state['nilai'] += 1
    st.session_state.s2 = 1
  else:
    st.session_state.s2 = 0
if (x3[0]):
  st.session_state.c3 = 1
  if (x3[1]):
    st.session_state['nilai'] += 1
    st.session_state.s3 = 1
  else:
    st.session_state.s3 = 0

    
if (st.session_state.s1 == 0 and st.session_state.c1 == 1 ):
    pass
    #y1 = stb.single_choice("Aksi reaksi bekerja pada satu benda", ["Benar", "Salah"], 1)
    if (y1[0]):
        pass
        #st.session_state.c1 = 1
        if (y1[1]):
          pass
            #st.write("Jawaban Benar")
            #st.session_state['nilai'] += 1
            #st.session_state.s1 = .5
        else:
          pass
            #st.session_state.s1 = 0

nil = 0
for i in range(4):
    nil += st.session_state['s'+str(i)]
st.write('Nilai Sesi = ', nil)
st.write('Nilai Kumulatif = ', st.session_state.nilai)
