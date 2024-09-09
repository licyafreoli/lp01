# Cálculo da Área do Retângulo

## Descrição

Este repositório contém um simples script Python projetado para calcular a área de um retângulo. O script pede ao usuário para inserir a base e a altura do retângulo e utiliza esses valores para calcular a área usando a fórmula:

\[ \text{Área} = \text{Base} \times \text{Altura} \]

O principal objetivo deste projeto é demonstrar como criar uma função básica em Python e interagir com o usuário através da entrada de dados e exibição de resultados.

## Como Funciona

O script realiza as seguintes etapas:
1. Solicita ao usuário que insira o valor da base do retângulo.
2. Solicita ao usuário que insira o valor da altura do retângulo.
3. Calcula a área do retângulo usando a fórmula mencionada.
4. Exibe o resultado na tela.

## Código

Aqui está o código Python incluído no repositório:

```python
# Função para calcular a área do retângulo
def calcular_area_retangulo(base, altura):
    return base * altura

# Solicita ao usuário a base do retângulo
base = float(input("Digite a base do retângulo (em unidades): "))

# Solicita ao usuário a altura do retângulo
altura = float(input("Digite a altura do retângulo (em unidades): "))

# Calcula a área usando a função
area = calcular_area_retangulo(base, altura)

# Exibe o resultado
print(f"A área do retângulo é: {area} unidades quadradas.")

## Como Executar
Certifique-se de ter o Python instalado em seu sistema. O script foi testado com Python 3.x.

Copie o código para um arquivo chamado, por exemplo, calcular_area_retangulo.py.

Abra um terminal ou prompt de comando.

Navegue até o diretório onde o arquivo foi salvo.

Execute o script com o comando:

bash
Copiar código
python main.py
Siga as instruções exibidas para inserir a base e a altura do retângulo.
