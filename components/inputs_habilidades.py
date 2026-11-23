import sys
from pathlib import Path

import streamlit as st

# verificação da raiz do projeto.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from regras.dnd_2024.habilidades import modificador_habilidades

NOMES_ATRIBUTOS = ("FOR", "DES", "CON", "INT", "SAB", "CAR")


# Atualiza o atributo do personagem com o valor armazenado no widget correspondente.
def atualizar_atributos(nome: str):
    chave_widget = f"_atributo_{nome}"
    st.session_state["personagem"]["atributos"][nome] = (st.session_state[chave_widget])


def renderizar_atributos():
    # Obtém as pontuações dos atributos armazenadas no estado do personagem.
    pontuacoes = st.session_state["personagem"]["atributos"]
    for nome in NOMES_ATRIBUTOS:
        chave_widget = f"_atributo_{nome}"

        # Inicializa a chave auxiliar com a pontuação atual, caso ainda não exista.
        if chave_widget not in st.session_state:
            st.session_state[chave_widget] = pontuacoes[nome]

        # Exibe o campo de edição do atributo, limitado a valores entre 1 e 20.
        st.number_input(
            label=nome,
            min_value=1,
            max_value=20,
            step=1,
            key=chave_widget,
            on_change=atualizar_atributos,
            args=(nome,)
        )

        # Exibe o modificador com sinal explícito, inclusive para valores positivos.
        st.caption(
            f"Modificador: {modificador_habilidades(pontuacoes[nome]):+d}"
        )

    # Organiza cada pontuação e seu modificador para uso por outras partes da aplicação.
    atributos = {
        nome: {
            "valor": valor,
            "mod": modificador_habilidades(valor)
        }

        for nome, valor in pontuacoes.items()
    }

    return atributos
