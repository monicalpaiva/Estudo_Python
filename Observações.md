# **Python 3 – Mundo 1**
## PRIMEIROS PASSOS
print("Olá, mundo") </br>
nome = input("Qual seu nome?") </br>
print("É um prazer te conhecer, "+ nome) </br>

nome = "Monica" </br>
idade = 35 </br>
peso = 83 </br>

print("Meu nome é", nome, "com idade", idade, "e peso", 83,".") </br>

"""
Tipos primitivos e saída de dados

str => string

int => inteiro

float => flutuante

bool => boleano
"""

num01 = int(input("digite um numero")) </br>
num02 = int(input("digite mais um numero")) </br>
print(type(num01))  </br>
print(num01+num02) </br>
soma = num01 +num02 </br>
print("a soma entre {} e {} vale: {}".format(num01, num02, soma)) </br>
numero = input("digite algo") </br>
print(numero.isupper()) </br>

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

nome=input("Qual seu nome?") </br>
print("Olá,{:20}!" .format(nome)) </br>
print("Olá,{:>20}!" .format(nome)) </br>
print("Olá,{:<20}!" .format(nome)) </br>
print("Olá,{:^20}!" .format(nome)) </br>
print("Olá,{:=^20}!" .format(nome)) </br>
print('='*20) </br>

"""
saída:
Qual seu nome?monica
Olá,monica              !
Olá,              monica!
Olá,monica              !
Olá,       monica       !
Olá,=======monica=======!
""""

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

## UTILIZANDO MÓDULOS

import "class"
From "class" import "subclass"

math
ceil -> arredondar para cima
floor -> arredondar para baixo
trunc -> truncamneto
pow -> potencia
sqrt -> raiz quadrada
factorial -> fatorial

import math 
From math import sqrt
From math import sqrt,ceil

https://docs.python.org/3/library/index.html

import math
numero = int(input("digite um numero: "))
raiz = math.sqrt(numero)
print("A raiz de {} é {}" .format(numero, math.ceil(raiz)))

SAÍDA:
digite um numero: 35
A raiz de 35 é 6
########################

import random

num = random.randint(1,10)
print (num)

-> saída será um numero aleatório de 1 a 10