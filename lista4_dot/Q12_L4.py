#INSTITUTO FEDERAL DE EDUCAÇÃO, CIÊNCIA E TECNOLOGIA DO PIAUÍ
#CAMPUS TERESINA CENTRAL
#TÉCNICO EM DESENVOLVIMENTO DE SISTEMAS
#PROF.: OSIRES PIRES COELHO FILHO
#ALUNO: PEDRO AUGUSTO RODRIGUES MELO
#DISCIPLINA: DESENVOLVIMENTO ORIENTADO A TESTES
#DATA: 19/12/2024

# Faça uma função que recebe 2 valores inteiros por parâmetro e retorna-os ordenados em ordem crescente.

def ordenados(a, b):
    if type(a) != int or type(b) != int:
        return Exception
    if a > b:
        return (b, a)
    elif b > a:
        return (a, b)

assert ordenados(3, 1) == (1, 3)
assert ordenados(70, 7) == (7, 70)
assert ordenados(1, 8) == (1, 8)

assert ordenados(0, "w") == Exception
assert ordenados(True, 1) == Exception
assert ordenados(2.5, 4.5) == Exception

print("Todos os testes ok.")