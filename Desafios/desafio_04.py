"""
DESAFIO 04
Ler algo e mostrar na tela o seu tipo primirivo e todas as informações possiveis sobre ele.
"""

algo = input("Escreva algo...")
print(type(algo))
print("É número?", algo.isalnum())
print("É alfanumérico?", algo.isalpha())
print("É ASCII?",algo.isascii())
print("É decimal?", algo.isdecimal())
print("É digital?", algo.isdigit())
print("É identificador?", algo.isidentifier())
print("Está em caixa baixa?", algo.islower())
print("É numerico?", algo.isnumeric())
print("Pode imprimir?", algo.isprintable())
print("É espaço?", algo.isspace())
print("É título?", algo.istitle())
print("Está em caixa alta?", algo.isupper())