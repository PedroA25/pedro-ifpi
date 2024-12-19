#INSTITUTO FEDERAL DE EDUCAÇÃO, CIÊNCIA E TECNOLOGIA DO PIAUÍ
#CAMPUS TERESINA CENTRAL
#TÉCNICO EM DESENVOLVIMENTO DE SISTEMAS
#PROF.: OSIRES PIRES COELHO FILHO
#ALUNO: PEDRO AUGUSTO RODRIGUES MELO
#DISCIPLINA: DESENVOLVIMENTO ORIENTADO A TESTES
#DATA: 04/12/2024

# Faça uma função que recebe a idade de uma pessoa em anos, meses e dias e retorna essa idade expressa em dias.

def idade(a, m, d):
    if type(a) != int or type(m) != int or type(d) != int:
        return Exception
    elif a < 0 or m < 0 or d < 0:
        return Exception
    elif a > 122 or m > 11 or d > 30:
        return Exception
    idade = a * 365 + m *30 + d
    return idade


assert idade(1, 0, 0) == 365
assert idade(0, 1, 0) == 30
assert idade(0, 0, 15) == 15
assert idade(2, 6, 15) == 925

assert idade(0, 0, 0) == 0
assert idade(0, 11, 30) == 360
assert idade(100, 0, 0) == 36500

assert idade(24, 12, 0) == Exception
assert idade(-1, 0, 0) == Exception
assert idade(0, 12, 0) == Exception
assert idade(0, 0, 31) == Exception
assert idade("dias", 11, 30) == Exception

print("Todos os testes ok!")