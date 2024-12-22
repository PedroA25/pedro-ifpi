#INSTITUTO FEDERAL DE EDUCAÇÃO, CIÊNCIA E TECNOLOGIA DO PIAUÍ
#CAMPUS TERESINA CENTRAL
#TÉCNICO EM DESENVOLVIMENTO DE SISTEMAS
#PROF.: OSIRES PIRES COELHO FILHO
#ALUNO: PEDRO AUGUSTO RODRIGUES MELO
#DISCIPLINA: DESENVOLVIMENTO ORIENTADO A TESTES
#DATA: 19/12/2024

# Faça uma função que leia um número não determinado de valores positivos e retorna a média aritmética dos mesmos.

def numero(X):
    if type(x) != int and type(x) != float:
        return Exception
    if x < 1:
        return Exception 
    quantidade = len(x)
    media = sum(x)/quantidade
    return media


print("Todos os testes ok.")