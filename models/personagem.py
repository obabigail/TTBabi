# modelo simples do personagem

NOMES_ATRIBUTOS = ("FOR", "DES", "CON", "INT", "SAB", "CAR")

def criar_personagem() -> dict:
    return {
        "nome": "",
        "nivel": 1,
        "atributos": {
            nome: 10 for nome in NOMES_ATRIBUTOS
        }
    }
