def calcular_reajuste():
    # Solicita o salário atual do colaborador
    salario_atual = float(input("Informe o salário atual do colaborador: R$ "))

    # Define os percentuais de aumento de acordo com o salário atual
    if salario_atual <= 280.00:
        percentual_aumento = 20
    elif salario_atual <= 700.00:
        percentual_aumento = 15
    elif salario_atual <= 1500.00:
        percentual_aumento = 10
    else:
        percentual_aumento = 5

    # Calcula o valor do aumento e o novo salário
    valor_aumento = salario_atual * (percentual_aumento / 100)
    novo_salario = salario_atual + valor_aumento

    # Define a inflação do período
    inflacao = 3.8  # em percentual

    # Calcula o aumento real descontando a inflação
    aumento_real = valor_aumento - (salario_atual * (inflacao / 100))

    # Exibe os resultados
    print("\nResultados do reajuste:")
    print(f"1. Salário antes do reajuste: R$ {salario_atual:.2f}")
    print(f"2. Percentual de aumento aplicado: {percentual_aumento}%")
    print(f"3. Valor do aumento: R$ {valor_aumento:.2f}")
    print(f"4. Novo salário, após o aumento: R$ {novo_salario:.2f}")
    print(f"5. Valor do aumento real (descontado a inflação): R$ {aumento_real:.2f}")

# Chama a função principal
if __name__ == "__main__":
    calcular_reajuste()
