#INSTITUTO FEDERAL DE EDUCAÇÃO, CIÊNCIA E TECNOLOGIA DO PIAUÍ
#CAMPUS TERESINA CENTRAL
#TÉCNICO EM DESENVOLVIMENTO DE SISTEMAS
#PROF.: OSIRES PIRES COELHO FILHO
#ALUNO: PEDRO AUGUSTO RODRIGUES MELO
#DISCIPLINA: DESENVOLVIMENTO ORIENTADO A TESTES
#DATA: 19/12/2024

# Escreva uma função que recebe por parâmetro um valor inteiro e positivo N e retorna o valor de S.
# S = 1 + 1/1! + 1⁄2! + 1/3! + 1 /N!

import math

def equacao(x):
    if type(x) != int or x <= 0:
        return Exception
    return round(sum(1/ math.factorial(i) for i in range(x + 1)), 2)

assert equacao(1) == 2
assert equacao(5) == 2.72
assert equacao(6) == 2.72
assert equacao(3) == 2.67

assert equacao(True) == Exception
assert equacao(-2) == Exception
assert equacao("e") == Exception
assert equacao(2.3) == Exception

print("Todos os testes ok.")