#INSTITUTO FEDERAL DE EDUCAÇÃO, CIÊNCIA E TECNOLOGIA DO PIAUÍ
#CAMPUS TERESINA CENTRAL
#TÉCNICO EM DESENVOLVIMENTO DE SISTEMAS
#PROF.: OSIRES PIRES COELHO FILHO
#ALUNO: PEDRO AUGUSTO RODRIGUES MELO
#DISCIPLINA: DESENVOLVIMENTO ORIENTADO A TESTES
#DATA: 19/12/2024

# Escreva uma função que recebe, por parâmetro, um valor inteiro e positivo e retorna o somatório desse valor.

def somatorio(x):
    if type(x) != int or x < 0:
        return Exception
    soma = 0
    for i in range(1, x+1):
        soma += i
    return soma

assert somatorio(1) == 1
assert somatorio(2) == 3
assert somatorio(3) == 6 

assert somatorio(-4) == Exception
assert somatorio("w") == Exception
assert somatorio(True) == Exception
assert somatorio(2.3) == Exception

print("Todos os testes ok")