from typing import Any
import streamlit as st
st.image("WAPP.png")
col1,col2,col3=st.columns(3)
with col2:
    st.subheader('Elige el laboratorio a analizar')
    seleccion=st.selectbox("",['Selecciona','Glucosa','Creatinina','Trigliceridos'])
if seleccion=="Selecciona":
    with col2:
        st.image('lab.png',None,250)
elif seleccion=="Glucosa":
    glu=st.number_input("Glucosa (mg/dl)",0,400,0,1)
    embarazo=st.checkbox("¿Estas embarazada?")
    if glu<=70 and glu >0:
        tol1,tol2,tol3,tol4,tol5=st.columns(5)
        with tol1:
            st.warning("tu azucar puede estar bajo los niveles normales, se guiere consumir algún alimento dulce como un jugo")
        with tol2:
            st.image("jugonaranja.jpg")
        with tol3:
            st.warning("Si utilizas insulina es probable que requieras una disminución de tus aportes de insulina")
        with tol4:
            st.error("Recuerda que si tu azucar está baja y el nivel de consciencia esta disminuido, no deben ingerirse alimentos vía oral, por el riesgo de broncoaspiración, contacta a los servicios de salud de inmediato")
    elif glu>=120 and embarazo==True:
        st.success("Estas embarazada")
        st.balloons()