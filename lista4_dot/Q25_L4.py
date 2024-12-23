#INSTITUTO FEDERAL DE EDUCAÇÃO, CIÊNCIA E TECNOLOGIA DO PIAUÍ
#CAMPUS TERESINA CENTRAL
#TÉCNICO EM DESENVOLVIMENTO DE SISTEMAS
#PROF.: OSIRES PIRES COELHO FILHO
#ALUNO: PEDRO AUGUSTO RODRIGUES MELO
#DISCIPLINA: DESENVOLVIMENTO ORIENTADO A TESTES
#DATA: 19/12/2024

# Escreva uma função que recebe, por parâmetro um valor inteiro e retorna o seu fatorial.

def fatorial(x):
    if type(x) != int or x < 0:
        return Exception
    fat = 1
    for i in range(1, x+1):
        fat *= i
    return fat

assert fatorial(0) == 1
assert fatorial(4) == 24
assert fatorial(5) == 120
assert fatorial(2) == 2

assert fatorial(-4) == Exception
assert fatorial(True) == Exception
assert fatorial(2.3) == Exception
assert fatorial("r") == Exception

print("Todos os testes ok.")