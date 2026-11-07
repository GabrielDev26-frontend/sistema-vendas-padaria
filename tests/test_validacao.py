"""Testes unitários da validação de vendas.

Equivalente direto do antigo test.js (que testava a função validarVenda em
JavaScript) — agora testando a função Python `validar_venda` em app.py.
"""
from app import validar_venda


def test_venda_valida():
    assert validar_venda("Pão", 2, 10) is True


def test_produto_vazio_invalido():
    assert validar_venda("", 2, 10) is False


def test_produto_so_espacos_invalido():
    assert validar_venda("   ", 2, 10) is False


def test_quantidade_zero_invalida():
    assert validar_venda("Pão", 0, 10) is False


def test_valor_zero_invalido():
    assert validar_venda("Pão", 2, 0) is False


def test_valor_nao_numerico_invalido():
    assert validar_venda("Pão", "abc", 10) is False
