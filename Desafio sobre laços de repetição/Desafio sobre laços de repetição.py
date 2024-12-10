def calcular_reajuste(salario_atual):
    # Determinar o percentual de aumento
    if salario_atual <= 280:
        percentual_aumento = 20
    elif salario_atual <= 700:
        percentual_aumento = 15
    elif salario_atual <= 1500:
        percentual_aumento = 10
    else:
        percentual_aumento = 5

    # Calcular o valor do aumento
    aumento = salario_atual * percentual_aumento / 100

    # Calcular o novo salário após o aumento
    novo_salario = salario_atual + aumento

    # Inflação do período
    inflacao = 3.8 / 100

    # Calcular o aumento real, descontando a inflação
    aumento_real = aumento * (1 - inflacao)

    # Exibir os resultados
    print(f"Salário antes do reajuste: R$ {salario_atual:.2f}")
    print(f"Percentual de aumento aplicado: {percentual_aumento}%")
    print(f"Valor do aumento: R$ {aumento:.2f}")
    print(f"Novo salário, após o aumento: R$ {novo_salario:.2f}")
    print(f"Valor do aumento real, descontando a inflação: R$ {aumento_real:.2f}")

# Receber o salário do colaborador
salario_atual = float(input("Digite o salário atual do colaborador: R$ "))
calcular_reajuste(salario_atual)
