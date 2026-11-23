import streamlit as st

from components.inputs_habilidades import NOMES_ATRIBUTOS, renderizar_atributos

if "personagem" not in st.session_state:
    st.session_state["personagem"] = {
        "atributos": {
            nome: 10 for nome in NOMES_ATRIBUTOS
        }
    }

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
