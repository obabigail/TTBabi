"""Testes da regra de modificadores de atributos de D&D 2024.

Execute a partir da raiz do projeto:
    python -m pytest tests/teste_habilidades.py -v

Estrutura esperada:
    regras/dnd_2024/habilidades.py  -> modificador_habilidades
    tests/tests_habilidades.py
"""

import pytest

from regras.dnd_2024.habilidades import modificador_habilidades


@pytest.mark.parametrize(
    ("pontos", "esperado"),
    [
        (1, -5),
        (2, -4),
        (3, -4),
        (8, -1),
        (9, -1),
        (10, 0),
        (11, 0),
        (12, 1),
        (13, 1),
        (15, 2),
        (20, 5),
        (29, 9),
        (30, 10),
    ],
)
def test_modificador_para_pontos_validos(pontos: int, esperado: int) -> None:
    """Confere valores de fronteira, pares, impares e modificadores negativos."""
    assert modificador_habilidades(pontos) == esperado


@pytest.mark.parametrize("pontos", [-100, -1, 0, 31, 100])
def test_rejeita_inteiros_fora_do_intervalo(pontos: int) -> None:
    """Um atributo fora do intervalo de 1 a 30 deve causar ValueError."""
    with pytest.raises(ValueError):
        modificador_habilidades(pontos)


@pytest.mark.parametrize(
    "pontos",
    [
        True,
        False,
        10.0,
        10.5,
        "10",
        None,
        [10],
        {"pontos": 10},
    ],
)
def test_rejeita_tipos_diferentes_de_int(pontos: object) -> None:
    """Inclusive bool, que em Python e uma subclasse de int."""
    with pytest.raises(TypeError):
        modificador_habilidades(pontos)  # type: ignore[arg-type]


def test_zero_e_modificador_valido() -> None:
    """Diferencia um resultado legitimo de zero de uma entrada invalida."""
    assert modificador_habilidades(10) == 0
    assert modificador_habilidades(11) == 0
    with pytest.raises(ValueError):
        modificador_habilidades(0)
