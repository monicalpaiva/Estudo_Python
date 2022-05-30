# **Python 3 – Mundo 1**
"""
PRIMEIROS PASSOS
"""
print("Olá, mundo")
nome = input("Qual seu nome?")
print("É um prazer te conhecer, "+ nome)

nome = "Monica"
idade = 35
peso = 83

print("Meu nome é", nome, "com idade", idade, "e peso", 83,".")
#########################################

"""
Tipos primitivos e saída de dados

str => string

int => inteiro

float => flutuante

bool => boleano
"""

num01 = int(input("digite um numero"))
num02 = int(input("digite mais um numero"))
print(type(num01)) 
print(num01+num02)
soma = num01 +num02
print("a soma entre {} e {} vale: {}".format(num01, num02, soma))
numero = input("digite algo")
print(numero.isupper())

"""
Operadores aritméticos

*   Soma +
*   Subtração -
*   Multiplicação *
*   Divisão /
*   Potência **
*   Divisão inteira //
*   Resto da divisão %

Ordem de procedencia

=> () 

=> **

=> *; / ; // ; % 
 
=> +-
"""
print(pow(5,2))

print('='*20)
nome=input("Qual seu nome?")
print("Olá,{:20}!" .format(nome))
print("Olá,{:>20}!" .format(nome))
print("Olá,{:<20}!" .format(nome))
print("Olá,{:^20}!" .format(nome))
print("Olá,{:=^20}!" .format(nome))
print('='*20)

"""
saída:

====================
Qual seu nome?monica
Olá,monica              !
Olá,              monica!
Olá,monica              !
Olá,       monica       !
Olá,=======monica=======!

"""

num01 = int(input("digite um numero:"))
num02 = int(input("digite outro numero:"))
soma = num01 + num02
multiplicacao = num01 * num02
divisao = num01 /num02
divisaointeira = num01//num02
potencia = num01**num02
print("A soma vale {}, \n a multiplicação vale {} \n e a divisão vale {:.2f}" .format(soma, multiplicacao, divisao), end=' ')
print("A divisão inteira vale {} \n e a potência vale {}" .format(divisaointeira, potencia))
#########################################
