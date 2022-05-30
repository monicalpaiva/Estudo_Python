"""
DESAFIO 12
Ler o preço de um produto e mostre seu novo preço com 5% de desconto
"""
preco = float(input("Digite o valor do produto:"))
novo_preco = preco - ((preco*5)/100)
print("O valor final do produto com desconto de 5% vale R$ {:.2f}." .format(novo_preco))