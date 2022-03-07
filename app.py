import streamlit as st
st.image("WAPP.png")
sol1,sol2,sol3=st.columns(3)
seleccion=st.selectbox("Laboratorios, elige el laboratorio que quieres analizar",['Selecciona','Glucosa','Urea','Creatinina','Trigliceridos','Colesterol total'])
if seleccion=="Selecciona":
    st.image('lab.png',None,250)
    st.balloons
    st.subheader("Hola baby")


