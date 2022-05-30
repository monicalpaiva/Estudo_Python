"""
DESAFIO 15

Escreva um programa que pergunte a quantidade de Km percorridos por um carro 
alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço 
a pagar, sabendo que o carro custa 60 reais por dia e 0,15 centavos por km 
rodado
"""
dia = float(input("Quantos dias alugado?"))
km = float(input("Quantos km precorridos?"))
valor_pagar = (dia*60) + (km*0.15)

print("Total a pagar é R${:.2f}" .format(valor_pagar))