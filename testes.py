import pytest
from calculadora_completa import CalculadoraCompleta

@pytest.fixture
def calculadora():
    c = CalculadoraCompleta()
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

def testCelsiusParaFahrenheit(calculadora):
    assert calculadora.celsiusParaFahrenheit(30) == 86.0

def testFahrenheitParaCelsius(calculadora):
    assert calculadora.fahrenheitParaCelsius(86) == 30.0

def testHistorico(calculadora):
    calculadora.soma(5, 3)
    calculadora.soma(-5, -3)
    calculadora.multiplicacao(15, 4)
    calculadora.divisao(15, 4)
    calculadora.raiz(1024, 5)
    calculadora.celsiusParaFahrenheit(30)
    calculadora.fahrenheitParaCelsius(86)
    assert len(calculadora.getHistorico()) == 7

def testLimpezaHistorico(calculadora):
    calculadora.soma(5, 3)
    calculadora.soma(-5, -3)
    calculadora.multiplicacao(15, 4)
    calculadora.divisao(15, 4)
    calculadora.raiz(1024, 5)
    calculadora.celsiusParaFahrenheit(30)
    calculadora.fahrenheitParaCelsius(86)
    calculadora.limparHistorico()
    assert len(calculadora.getHistorico()) == 0
    



# python -m pytest testes.py
# python -m coverage run -m pytest testes.py
# python -m coverage report
# make test e make run 