"""
DESAFIO 13
Ler o salário de um funcionário e mostra seu novo salário, com 15% de aumento.
"""
salario = float(input("Digite o seu salário atual:"))
novo_salario = salario + ((salario * 15)/100)

print("O valor do novo salário é R$ {:.2f}" .format(novo_salario))