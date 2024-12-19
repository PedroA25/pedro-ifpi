#INSTITUTO FEDERAL DE EDUCAÇÃO, CIÊNCIA E TECNOLOGIA DO PIAUÍ
#CAMPUS TERESINA CENTRAL
#TÉCNICO EM DESENVOLVIMENTO DE SISTEMAS
#PROF.: OSIRES PIRES COELHO FILHO
#ALUNO: PEDRO AUGUSTO RODRIGUES MELO
#DISCIPLINA: DESENVOLVIMENTO ORIENTADO A TESTES
#DATA: 04/12/2024

# Faça uma função que verifique se um valor é perfeito ou não. Um valor é dito perfeito quando ele é igual à soma dos seus divisores excetuando ele próprio.
# (Ex: 6 é perfeito, 6 = 1 + 2 + 3, que são seus divisores). A função deve retornar um valor booleano.

def perfeito(x):
    soma = 0
    if type(x) != int or x <= 1:
        return Exception
    for i in range(1, x):
        if x % i == 0:
            soma += i
    if soma == x:
        return True
    return False

assert perfeito(6) == True
assert perfeito(28) == True
assert perfeito(496) == True
assert perfeito(7) == False
assert perfeito(9) == False
assert perfeito(8) == False

assert perfeito("x") == Exception
assert perfeito(1) == Exception
assert perfeito(-23) == Exception
assert perfeito(True) == Exception

print("Todos os testes ok!")