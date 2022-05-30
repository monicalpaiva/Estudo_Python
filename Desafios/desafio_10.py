
"""Desafio 10

Ler quanto dinheiro tem na carteira e mostre quantos dólares ela pode comprar

USS = 1,00
R$ = 3,27
"""
real = float(input("Digite o valor que tem na carteira: R$"))
dolar = real / 3.27

print("Você tem {:.2f} dolares!" .format(dolar))