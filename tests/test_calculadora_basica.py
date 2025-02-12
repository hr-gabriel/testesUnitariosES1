import pytest
from calculadora_basica import CalculadoraBasica

@pytest.fixture
def calculadora():
    c = CalculadoraBasica()
    return c

def testSomaPositivos(calculadora):
    assert calculadora.soma(5, 3) == 8.0

def testSomaNegativos(calculadora):
    assert calculadora.soma(-5, -3) == -8.0

def testSubtracao(calculadora):
    assert calculadora.subtracao(5, 7) == -2.0

def testSubtracaoComNegativo(calculadora):
    assert calculadora.subtracao(5, -3) == 8.0

def testMultiplicacao(calculadora):
    assert calculadora.multiplicacao(15, 4) == 60.0

def testDivisao(calculadora):
    assert calculadora.divisao(15, 4) == 3.75

def testDivisaoPorZero(calculadora):
    with pytest.raises(ArithmeticError):
        calculadora.divisao(2, 0)