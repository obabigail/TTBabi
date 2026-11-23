# Define os modificadores de habilidade de acordo com o livro de regras do D&D 2024
def modificador_habilidades(pontos: int) -> int:
    if type(pontos) != int:
        raise TypeError("seus pontos devem ser números inteiros. convertendo modificador para 0")
    elif pontos <= 0 or pontos > 30:
        raise ValueError("seus pontos devem ser maiores que 0 e menores que 30. converntendo modificador para 0")
    else:
        # a operação '//' arredonda valores para baixo
        return (pontos - 10) // 2
