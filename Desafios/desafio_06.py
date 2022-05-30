"""
DESAFIO 06
Ler um número e mostra o seu dobro, triplo e a raiz quadrada
"""
numero = int(input("Digite um número:"))
raiz = pow(numero,(1/2))
print("O dobro do número {} é {}, seu triplo é {} e sua raiz é {:.2f}" .format(numero, (numero*2), (numero*3), raiz))