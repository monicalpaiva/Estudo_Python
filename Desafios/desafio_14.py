"""
DESAFIO 14
Escreva um programa que converta uma temperatura digitando em graus Celsius 
e converta para graus Fahrenheit.
"""
celsius = float(input("Qual temperatuda em Celsius?"))
fahrenheit = ((celsius * 1.8) + 32)

print("No momento está apresentando {} ºF!" .format(fahrenheit))