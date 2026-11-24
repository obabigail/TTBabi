
from models.personagem import criar_personagem

def test_personagem_inicial():
    personagem = criar_personagem()

    assert personagem["nome"] == ""
    assert personagem["nivel"] == 1
    assert len(personagem["atributos"]) == 6

    for valor in personagem["atributos"].values():
        assert valor == 10

def test_personagens_independentes():
    primeiro = criar_personagem()
    segundo = criar_personagem()

    primeiro["atributos"]["FOR"] = 18

    assert segundo["atributos"]["FOR"] == 10
