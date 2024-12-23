#INSTITUTO FEDERAL DE EDUCAÇÃO, CIÊNCIA E TECNOLOGIA DO PIAUÍ
#CAMPUS TERESINA CENTRAL
#TÉCNICO EM DESENVOLVIMENTO DE SISTEMAS
#PROF.: OSIRES PIRES COELHO FILHO
#ALUNO: PEDRO AUGUSTO RODRIGUES MELO
#DISCIPLINA: DESENVOLVIMENTO ORIENTADO A TESTES
#DATA: 19/12/2024

# Escreva uma função que recebe por parâmetro um valor inteiro e positivo N e retorna o valor de S.
# S = 2/4 + 5/5 + 10/6 + 17/7 + 26/8 + ... +(n2+1)/(n+3)

def equacao(n):
    if type(n) != int or n < 1:
        return Exception
    return round(sum((i**2 + 1) / (i + 3) for i in range(1, n+1)), 2) 

assert equacao(1) == 0.5
assert equacao(4) == 5.6
assert equacao(5) == 8.85
assert equacao(20) == 169.01

assert equacao(True) == Exception
assert equacao("w") == Exception
assert equacao(2.4) == Exception
assert equacao(-3) == Exception

print("Todos os testes ok.")