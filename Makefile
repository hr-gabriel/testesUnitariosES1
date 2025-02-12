.PHONY: test run all clean

# Executar os testes com pytest
test:
	@echo "Executando testes..."
	python -m pytest testes.py

# Rodar o programa principal (main.py)
run:
	@echo "Rodando o programa Calculadora..."
	python main.py

# Rodar testes e depois o programa
all: test run

# Limpar arquivos temporários e caches do Python
clean:
	@echo "Limpando arquivos temporários..."
	find . -type d -name "__pycache__" -exec rm -rf {} +
	rm -rf .pytest_cache
