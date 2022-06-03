"""
DESAFIO 18

Ler um ângulo qualquer e mostre na tela o valor do seno, cosseno e 
tangente desse angulo
"""

import math

angulo = (float(input("Digite o ângulo: ")))

seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print("De acordo com o angulo informado ({:.2f}rad), \n Temos como seno {:.2f}, \n Temos como cosseno {:.2f} \n Temos como tangente {:.2f}" .format(angulo, seno, cosseno,tangente))