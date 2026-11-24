import streamlit as st

from components.inputs_habilidades import renderizar_atributos
from models.personagem import criar_personagem

if "personagem" not in st.session_state:
    st.session_state["personagem"] = criar_personagem()

etapa = st.radio(
    "Etapa da criação",
    ["Atributos", "Revisão"],
    horizontal=True
)

if etapa == "Atributos":
    atributos = renderizar_atributos()
    st.json(atributos)

else:
    st.subheader("Ficha do personagem")
    st.json(st.session_state["personagem"])
