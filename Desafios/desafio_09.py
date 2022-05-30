
"""
DESAFIO 09
Ler um numero qualquer e mostre a sua tabuada
"""
numero = int(input("Digite um numero:"))
nome = "TABUADA"
caractere = "||"
numero0 = numero*0
numero1 = numero*1
numero2 = numero*2
print('='*20)
print("{:=^20}" .format(nome))
print('='*20)
print("{} {} x 0 = {}" .format(caractere,numero,numero0))
print("{} {} x 1 = {}" .format(caractere,numero,numero1))
print("{} {} x 2 = {}" .format(caractere,numero,numero2))
print("{} {} x {} = {}" .format(caractere,numero,3,(numero*3)))
print("{} {} x {} = {}" .format(caractere,numero,4,(numero*4)))
print("{} {} x {} = {}" .format(caractere,numero,5,(numero*5)))
print("{} {} x 6" .format(caractere,numero),"=",(numero*6))
print("{} {} x 7" .format(caractere,numero),"=",(numero*7))
print("{} {} x 8" .format(caractere,numero),"=",(numero*8))
print("{} {} x 9" .format(caractere,numero),"=",(numero*9))
print("{} {} x 10" .format(caractere,numero),"=",(numero*10))
print('='*20)