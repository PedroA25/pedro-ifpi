#INSTITUTO FEDERAL DE EDUCAÇÃO, CIÊNCIA E TECNOLOGIA DO PIAUÍ
#CAMPUS TERESINA CENTRAL
#TÉCNICO EM DESENVOLVIMENTO DE SISTEMAS
#PROF.: OSIRES PIRES COELHO FILHO
#ALUNO: PEDRO AUGUSTO RODRIGUES MELO
#DISCIPLINA: DESENVOLVIMENTO ORIENTADO A TESTES
#DATA: 19/12/2024

# Faça uma função que leia um número não determinado de valores positivos e retorna a média aritmética dos mesmos.

def numero(x):
    if any(isinstance(i, (bool, str)) or i <= 0 for i in x):
        return Exception
    if len(x) < 1:
        return Exception 
    quantidade = len(x)
    media = sum(x)/quantidade
    return media

assert numero([1, 2, 3, 4, 5]) == 3
assert numero([10, 20, 30]) == 20
assert numero([0, 0, 0]) == Exception
assert numero([100]) == 100

assert numero([-4, 5, 3]) == Exception
assert numero([True, 2, 4]) == Exception
assert numero([]) == Exception
assert numero(["e", 4]) == Exception

print("Todos os testes ok.")