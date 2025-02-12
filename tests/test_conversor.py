import pytest
from conversor import Conversor

@pytest.fixture
def conversor():
    c = Conversor()
    return c

def testCelsiusParaFahrenheit(conversor):
    assert conversor.celsiusParaFahrenheit(30) == 86.0

def testFahrenheitParaCelsius(conversor):
    assert conversor.fahrenheitParaCelsius(86) == 30.0

   
