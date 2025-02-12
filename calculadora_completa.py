from calculadora_basica import CalculadoraBasica
from calculadora_cientifica import CalculadoraCientifica
from conversor import Conversor

class CalculadoraCompleta:
    def __init__(self):
        self.calculadoraBasica = CalculadoraBasica()
        self.calculadoraCientifica = CalculadoraCientifica()
        self.conversor = Conversor()
        self.historicoResultados = []
    
    def adicionarAoHistorico(self, operacao):
        self.historicoResultados.append(operacao)
    
    def limparHistorico(self):
        self.historicoResultados.clear()
    
    def getHistorico(self):
        return self.historicoResultados
    
    # Operações básicas
    def soma(self, a, b):
        resultado = self.calculadoraBasica.soma(a, b)
        self.adicionarAoHistorico(f"{a} + {b} = {resultado}")
        return resultado
    
    def subtracao(self, a, b):
        resultado = self.calculadoraBasica.subtracao(a, b)
        self.adicionarAoHistorico(f"{a} - {b} = {resultado}")
        return resultado
    
    def multiplicacao(self, a, b):
        resultado = self.calculadoraBasica.multiplicacao(a, b)
        self.adicionarAoHistorico(f"{a} * {b} = {resultado}")
        return resultado
    
    def divisao(self, a, b):
        resultado = self.calculadoraBasica.divisao(a, b)
        self.adicionarAoHistorico(f"{a} / {b} = {resultado}")
        return resultado
    
    # Operações científicas
    def potencia(self, a, b):
        resultado = self.calculadoraCientifica.potencia(a, b)
        self.adicionarAoHistorico(f"{a} ^ {b} = {resultado}")
        return resultado
    
    def raiz(self, a, indice):
        resultado = self.calculadoraCientifica.raiz(a, indice)
        self.adicionarAoHistorico(f"{indice}√{a} = {resultado}")
        return resultado
    
    def fatorial(self, a):
        resultado = self.calculadoraCientifica.fatorial(a)
        self.adicionarAoHistorico(f"{a}! = {resultado}")
        return resultado
    
    # Conversor de temperatura
    def celsiusParaFahrenheit(self, valor_celsius):
        resultado = self.conversor.celsiusParaFahrenheit(valor_celsius)
        self.adicionarAoHistorico(f"{valor_celsius}°C para Fahrenheit = {resultado}")
        return resultado
    
    def fahrenheitParaCelsius(self, valor_fahrenheit):
        resultado = self.conversor.fahrenheitParaCelsius(valor_fahrenheit)
        self.adicionarAoHistorico(f"{valor_fahrenheit}°F para Celsius = {resultado}")
        return resultado