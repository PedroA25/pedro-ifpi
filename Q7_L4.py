#INSTITUTO FEDERAL DE EDUCAÇÃO, CIÊNCIA E TECNOLOGIA DO PIAUÍ
#CAMPUS TERESINA CENTRAL
#TÉCNICO EM DESENVOLVIMENTO DE SISTEMAS
#PROF.: OSIRES PIRES COELHO FILHO
#ALUNO: PEDRO AUGUSTO RODRIGUES MELO
#DISCIPLINA: DESENVOLVIMENTO ORIENTADO A TESTES
#DATA: 08/12/2024



def nadador(x):
    if type(x) != int or x < 5:
        return Exception
    if 5 < x <= 7:
        return 'Infantil A'
    elif 8 < x <= 10:
        return 'Infantil B'
    elif 10 < x <= 13:
        return 'Juvenil A'
    elif 14 < x <= 17:
        return 'Juvenil B'
    elif x >= 18:
        return 'Adulto'

assert nadador(6) == 'Infantil A'
assert nadador(9) == 'Infantil B'
assert nadador(12) == 'Juvenil A'
assert nadador(16) == 'Juvenil B'
assert nadador(20) == 'Adulto'

assert nadador(0) == Exception
assert nadador(2.5) == Exception
assert nadador(True) == Exception
assert nadador(-4) == Exception
assert nadador('x') == Exception

print("Todos os testes ok.")