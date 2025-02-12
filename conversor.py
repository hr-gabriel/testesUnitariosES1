class Conversor:
    def celsiusParaFahrenheit(self, valorCelsius):
        return (9.0/5) * valorCelsius + 32
    
    def fahrenheitParaCelsius(self, valorFahrenheit):
        return 5 * (valorFahrenheit - 32) / 9