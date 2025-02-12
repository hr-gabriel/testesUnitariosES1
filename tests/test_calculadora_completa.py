
import pytest
from calculadora_completa import CalculadoraCompleta

@pytest.fixture
def calculadora():
    c = CalculadoraCompleta()
    return c

# Testes Calculadora Completa (foco no histórico, uma vez que demais métodos já estão sendo testados através das classes específicas)
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
    calculadora.subtracao(-5, -3)
    calculadora.multiplicacao(15, 4)
    calculadora.divisao(15, 4)
    calculadora.raiz(1024, 5)
    calculadora.fatorial(5)
    calculadora.potencia(5, 3)
    calculadora.celsiusParaFahrenheit(30)
    calculadora.fahrenheitParaCelsius(86)
    calculadora.limparHistorico()
    assert len(calculadora.getHistorico()) == 0