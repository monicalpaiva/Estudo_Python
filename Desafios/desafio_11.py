"""
DESAFIO 11
Ler a largura e a altura de uma parede em metros. calcule a sua área e a quantidade de tinta necessária para pinta-la. sabendo que cada litro de tinra pinta uma área de 2m²
"""
largura = float(input("Digite o valor da largura:"))
altura = float(input("Digite o valor da altura:"))
area = altura * largura
tinta = area /2

print("A área total vale {} e será necessário {:.2f}litros de tinta para pintar!" .format(area, tinta))