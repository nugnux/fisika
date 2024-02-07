import streamlit as st

# Header
st.header('Nugroho :sparkles:')
st.subheader('Plot')

c1, c2, c3, c4 = st.columns(4)

with c1:
    x = st.number_input('x ',value=7)
    st.write('=>: ')
with c2:
    operator = st.selectbox(
        'operator',
        ('+', '-', 'x',':'),key='k1')
    st.write(':sparkles: ')
with c3:
    y = st.number_input('y ',value=11)
with c4:
    if (operator=='+'):
        z = x + y
    elif (operator=='+'):
        z = x - y
    elif (operator=='x'):
        z = x * y
    elif (operator==':'):
        z = x / y
    st.write('z' )    
    st.write('= ',z )




st.caption('Copyright © Nugroho Adi Pramono 2023')
