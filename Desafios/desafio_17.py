"""
DESAFIO 17

Ler o comprimento do cateto oposto e do cateto adjacente de um triângulo
 retângulo, calculando e mostrando o comprimento da hipotenusa.
"""

import math

oposto = float (input("Digite o cateto oposto: "))
adjacente = float (input("Digite o cateto adajcente: "))
hipotenusa = math.hypot(oposto,adjacente)

print("Valor da hipotenusa é {:.2f}" .format(hipotenusa))