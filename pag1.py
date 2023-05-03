import streamlit as st
import mlem


def show_footer():
    st.markdown("")


def main():

    st.title ("CALCOLA IL PREZZO")


    crim = st.number_input('Inserisci indice crim',0.0,1000.0,3.613524)
    zn = st.number_input('Inserisci indice zn',0.0,1000.0,11.363636)
    indus = st.number_input('Inserisci indice indus',0.0,1000.0,11.136779)
    chas = st.number_input('Inserisci indice chas',0.0,1000.0,0.069170)
    nox = st.number_input('Inserisci indice nox',0.0,1000.0,0.554695)
    rm = st.number_input('Inserisci indice rm',0.0,1000.0,6.284634)
    age = st.number_input('Inserisci indice age',0.0,1000.0,68.574901)
    dis = st.number_input('Inserisci indice dis',0.0,1000.0,3.795043)
    rad = st.number_input('Inserisci indice rad',0.0,1000.0,9.549407)  
    tax = st.number_input('Inserisci indice tax',0.0,1000.0,408.237154)
    pratio = st.number_input('Inserisci indice pratio',0.0,1000.0,18.455534)    
    b = st.number_input('Inserisci indice b',0.0,1000.0,356.674032)
    lstat = st.number_input('Inserisci indice lstat',0.0,1000.0,12.653063) 


    new_model = mlem.api.load('model_.mlem')


    pred= new_model.predict([[crim,zn,indus,chas,nox,rm,age,dis,rad,tax,pratio,b,lstat]])
    st.write(round(pred[0],2))



    
    show_footer()

if __name__ == "__main__":
    main()
