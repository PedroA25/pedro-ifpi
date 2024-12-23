#INSTITUTO FEDERAL DE EDUCAÇÃO, CIÊNCIA E TECNOLOGIA DO PIAUÍ
#CAMPUS TERESINA CENTRAL
#TÉCNICO EM DESENVOLVIMENTO DE SISTEMAS
#PROF.: OSIRES PIRES COELHO FILHO
#ALUNO: PEDRO AUGUSTO RODRIGUES MELO
#DISCIPLINA: DESENVOLVIMENTO ORIENTADO A TESTES
#DATA: 19/12/2024

# Faça uma função que recebe, por parâmetro, um valor inteiro e positivo e retorna o número de divisores desse valor.

def divisores(x):
    if type(x) != int or x < 1:
        return Exception
    else:
        L = []
        for i in range(1, x+1):
            if x % i == 0:
                L.append(i)
    return len(L)

assert divisores(1) == 1
assert divisores(6) == 4
assert divisores(16) == 5
assert divisores(25) == 3

assert divisores(True) == Exception
assert divisores("w") == Exception
assert divisores(2.3) == Exception
assert divisores(-3) == Exception

print("Todos os testes ok.")