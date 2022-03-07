from email.utils import collapse_rfc2231_value
from operator import truth
import iniconfig
from matplotlib import container
import streamlit as st
st.image("WAPP.png")
st.subheader("Labapp")
st.markdown("Elige el laboratorio que quieres analizar")
sol1,sol2,sol3=st.columns(3)
seleccion=st.selectbox("Laboratorios",['Biometría hemática','Química sanguinea','Hormonas tiroideas'])
inicio=st.button("Iniciamos")

if seleccion=="Biometría hemática" and inicio==True:
    @st.cache(persist=True)
    Leu=st.slider("Leucocitos cel/mm3",1,700000)


