#INSTITUTO FEDERAL DE EDUCAÇÃO, CIÊNCIA E TECNOLOGIA DO PIAUÍ
#CAMPUS TERESINA CENTRAL
#TÉCNICO EM DESENVOLVIMENTO DE SISTEMAS
#PROF.: OSIRES PIRES COELHO FILHO
#ALUNO: PEDRO AUGUSTO RODRIGUES MELO
#DISCIPLINA: DESENVOLVIMENTO ORIENTADO A TESTES
#DATA: 19/12/2024

# Escreva uma função que recebe, por parâmetro, dois valores X e Z e calcula e retorna Xz.
# (sem utilizar funções ou operadores de potência prontos)

def potencia(X, Z):
    if type(X) != int and type(X) != float:
        return Exception
    if type(Z) != int or Z < 0:
        return Exception
    xz = 1
    for i in range(Z):
        xz *= X
    return xz

print(potencia(-2, 0))

print("Todos os testes ok.")