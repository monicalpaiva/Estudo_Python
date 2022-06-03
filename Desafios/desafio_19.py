"""
DESAFIO 19

Um professor que sortear um dos seus quantro alunos para pagar o quadro.
Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome 
do escohido.
"""

import random

aluno01 = input("Escreva o nome do primeiro aluno: ")
aluno02 = input("Escreva o nome do primeiro aluno: ")
aluno03 = input("Escreva o nome do primeiro aluno: ")
aluno04 = input("Escreva o nome do primeiro aluno: ")

print("O aluno que irá apagar o quadro é ", random.choice([aluno01, aluno02, aluno03, aluno04]))