#INSTITUTO FEDERAL DE EDUCAÇÃO, CIÊNCIA E TECNOLOGIA DO PIAUÍ
#CAMPUS TERESINA CENTRAL
#TÉCNICO EM DESENVOLVIMENTO DE SISTEMAS
#PROF.: OSIRES PIRES COELHO FILHO
#ALUNO: PEDRO AUGUSTO RODRIGUES MELO
#DISCIPLINA: DESENVOLVIMENTO ORIENTADO A TESTES
#DATA: 19/12/2024

# Escreva uma função que recebe por parâmetro um valor inteiro e positivo N e retorna o valor de S.
# S = 1 + 1⁄2 + 1/3 + 1⁄4 + 1/5 + 1/N.

def equacao(x):
    if type(x) != int or x < 0:
        return Exception
    return round(sum(1/i for i in range(1, x+1)), 2)

assert equacao(1) == 1
assert equacao(2) == 1.5
assert equacao(3) == 1.83
assert equacao(100) == 5.19

assert equacao(-2) == Exception
assert equacao("w") == Exception
assert equacao(True) == Exception
assert equacao(2.4) == Exception

print("Todos os testes ok.")