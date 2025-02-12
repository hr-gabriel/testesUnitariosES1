<p align="center"><strong>Nome: Gabriel Henrique Rodrigues    RA: 813345</strong></p>
<br><br>

O projeto implementa uma **calculadora completa** com funções **básicas, científicas** e um **conversor de medidas**.  
As funcionalidades (classes) estão separadas em diferentes arquivos `.py`.  

---

# Funcionalidades  

## **Operações básicas**  
- Soma  
- Subtração  
- Multiplicação  
- Divisão  

## **Operações científicas**  
- Potência  
- Raiz  
- Fatorial  

## **Conversão de medidas**  
- Celsius -> Fahrenheit  
- Fahrenheit -> Celsius  

##  **Histórico de operações**  
- Visualizar operações realizadas  
- Limpar histórico  



# Como Executar a aplicação e os testes

- É importante ter o `Python 3` e o `Make` instalados no computador
- Os testes foram feitos usando `pytest`, então pode ser necessário executar `pip install pytest` no terminal, para garantir que os testes serão executados corretamente
- Abrir o terminal no diretório em que se encontram os arquivos do programa
  - `make test` para executar os testes
  - `make run`para executar o programa
 
- Também é possível verificar os testes de cobertura
  - Para isso, executar `pip install coverage` no terminal para instalar o Coverage
  - `python -m coverage run -m pytest tests/` para executar o teste de cobertura
  - `python -m coverage report` para visualizar a cobertura dos testes






