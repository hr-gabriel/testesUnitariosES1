import pytest
from calculadora_cientifica import CalculadoraCientifica

@pytest.fixture
def calculadora():
    c = CalculadoraCientifica()
    return c

def testPotencia(calculadora):
    assert calculadora.potencia(2, 10) == 1024

def testPotenciaBaseZeroEExpoenteNegativo(calculadora):
    with pytest.raises(ArithmeticError):
        calculadora.potencia(0, -10)

def testPotenciaBaseNegativaEExpoenteFracionario(calculadora):
    with pytest.raises(ArithmeticError):
        calculadora.potencia(-2, -0.5)

def testRaiz(calculadora):
    assert calculadora.raiz(1024, 5) == 4

def testRaizNegativa(calculadora):
    with pytest.raises(ArithmeticError):
        calculadora.raiz(-16, 2)

def testFatorial(calculadora):
    assert calculadora.fatorial(5) == 120

def testFatorialZeroEUm(calculadora):
    assert calculadora.fatorial(0) == 1
    assert calculadora.fatorial(1) == 1

def testFatorialNegativo(calculadora):
    with pytest.raises(ValueError):
        calculadora.fatorial(-5)