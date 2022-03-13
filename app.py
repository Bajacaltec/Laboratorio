import streamlit as st
st.image("WAPP.png")
seleccion=st.selectbox("Laboratorios, elige el laboratorio que quieres analizar",['Selecciona','Glucosa','Urea','Creatinina','Trigliceridos','Colesterol total'])
col1,col2,col3=st.columns(3)
tol1,tol2,tol3,tol4,tol5=st.columns(5)
if seleccion=="Selecciona":
    with col2:
        st.image('lab.png',None,250)
elif seleccion=="Glucosa":
    glu=st.number_input("Glucosa (mg/dl)",0,400,0,1)
    if glu<=70 and glu >0:
        st.warning("tu azucar puede estar bajo los niveles normales, se guiere consumir algún alimento dulce como un jugo")
        with tol1:
            st.image("jugonaranja.jpg")
        st.subheader("Si utilizas insulina es probable que requieras una disminución de tus aportes de insulina")


