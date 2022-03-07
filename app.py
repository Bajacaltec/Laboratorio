from email.utils import collapse_rfc2231_value
from operator import truth
import iniconfig
from matplotlib import container
import streamlit as st
st.image("WAPP.png")
sol1,sol2,sol3=st.columns(3)
seleccion=st.selectbox("Laboratorios, elige el laboratorio que quieres analizar",['Selecciona','Glucosa','Urea','Creatinina','Trigliceridos','Colesterol total'])
if seleccion=="Selecciona":
    st.image('Lab.png',None,250)


