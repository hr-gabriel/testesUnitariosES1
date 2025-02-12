class CalculadoraCientifica:
    def potencia(self, a, b):
        if a == 0 and b <= 0:
            raise ArithmeticError("Potência indefinida! Base 0 com expoente menor ou igual a 0.")
        if a < 0 and not isinstance(b, int):
            raise ArithmeticError("Potência indefinida! Base negativa com expoente fracionário.")
        return a ** b
    
    def raiz(self, a, indice):
        if a < 0:
            raise ArithmeticError("Erro! Raízes de números negativos não são permitidas no programa.")
        return self.potencia(a, 1 / indice)
    
    def fatorial(self, a):
        if a < 0:
            raise ValueError("Erro! O valor deve ser um número inteiro e maior ou igual que zero")
        elif a == 1 or a == 0:
            return 1
        else:
            return a * self.fatorial(a-1)