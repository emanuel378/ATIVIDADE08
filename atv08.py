# Imagine que você está em uma viagem para os Estados Unidos e precisa converter o valor em reais para dólares. Crie um programa que receba o valor em reais e a taxa de câmbio atual, e exiba o valor equivalente em dólares.
reais = float(input( "Digite o valor em reais:"))
taxa = 0.18
resultado = reais*taxa
print(f"Voce tem us:{resultado: .3}")