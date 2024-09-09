# Função para calcular a área do retângulo
def calcular_area_retangulo(base, altura):
    return base * altura

# base do retângulo
base = float(input("Digite a base do retângulo (em unidades): "))

# altura do retângulo
altura = float(input("Digite a altura do retângulo (em unidades): "))

# Calcula a área usando a função
area = calcular_area_retangulo(base, altura)

# Exibe o resultado
print(f"A área do retângulo é: {area} unidades quadradas.")
