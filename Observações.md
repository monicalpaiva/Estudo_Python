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
Qual seu nome?monica </br>
Olá,monica              ! </br>
Olá,              monica! </br>
Olá,monica              ! </br>
Olá,       monica       ! </br>
Olá,=======monica=======! </br>
"""

num01 = int(input("digite um numero:")) </br>
num02 = int(input("digite outro numero:")) </br>
soma = num01 + num02 </br>
multiplicacao = num01 * num02 </br>
divisao = num01 /num02 </br>
divisaointeira = num01//num02 </br>
potencia = num01**num02 </br>
print("A soma vale {}, \n a multiplicação vale {} \n e a divisão vale
{:.2f}" .format(soma, multiplicacao, divisao), end=' ') </br>
print("A divisão inteira vale {} \n e a potência vale {}" .format(divisaointeira, potencia))

## UTILIZANDO MÓDULOS

import "class"</br>
From "class" import "subclass"</br>

math</br>
ceil -> arredondar para cima </br>
floor -> arredondar para baixo </br>
trunc -> truncamneto </br>
pow -> potencia </br>
sqrt -> raiz quadrada </br>
factorial -> fatorial </br>

import math  </br>
From math import sqrt </br>
From math import sqrt,ceil </br>

https://docs.python.org/3/library/index.html

import math </br>
numero = int(input("digite um numero: ")) </br>
raiz = math.sqrt(numero) </br>
print("A raiz de {} é {}" .format(numero, math.ceil(raiz))) </br>

"""

SAÍDA: </br>
digite um numero: 35 </br>
A raiz de 35 é 6 </br>

"""

import random </br>

num = random.randint(1,10) </br>
print (num) </br>
-> saída será um numero aleatório de 1 a 10