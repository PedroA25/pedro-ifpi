#INSTITUTO FEDERAL DE EDUCAÇÃO, CIÊNCIA E TECNOLOGIA DO PIAUÍ
#CAMPUS TERESINA CENTRAL
#TÉCNICO EM DESENVOLVIMENTO DE SISTEMAS
#PROF.: OSIRES PIRES COELHO FILHO
#ALUNO: PEDRO AUGUSTO RODRIGUES MELO
#DISCIPLINA: DESENVOLVIMENTO ORIENTADO A TESTES
#DATA: 03/12/2024

# Faça uma função que recebe por parâmetro o raio de uma esfera e calcula o seu volume (v = 4/3 * PI * R**3).

import math

def volume(r):
    if type(r) != int and type(r) != float:
        return Exception
    elif r <= 0:
        return Exception
    else:
        v = 4/3 * math.pi * r**3
        return round(v, 3)


assert volume(20) == 33510.322
assert volume(3) == 113.097
assert volume(30.4) == 117681.816
assert volume(4.5) == 381.704

assert volume("web") == Exception
assert volume(0) == Exception
assert volume(-3) == Exception
assert volume(True) == Exception

print("Todos os testes ok!")


