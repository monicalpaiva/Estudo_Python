"""
DESAFIO 20

O mesmo professor do desafio anterior quer sortear a ordem de 
apresentação dos alunos. Faça um programa que leia o nome dos quatro 
alunos e mostra a ordem sorteada.
"""
import random

aluno01 = input("Escreva o nome do primeiro aluno: ")
aluno02 = input("Escreva o nome do primeiro aluno: ")
aluno03 = input("Escreva o nome do primeiro aluno: ")
aluno04 = input("Escreva o nome do primeiro aluno: ")

alunos = [aluno01, aluno02, aluno03, aluno04]
random.shuffle(alunos)

print("A sequencia é ", alunos)