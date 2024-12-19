#INSTITUTO FEDERAL DE EDUCAÇÃO, CIÊNCIA E TECNOLOGIA DO PIAUÍ
#CAMPUS TERESINA CENTRAL
#TÉCNICO EM DESENVOLVIMENTO DE SISTEMAS
#PROF.: OSIRES PIRES COELHO FILHO
#ALUNO: PEDRO AUGUSTO RODRIGUES MELO
#DISCIPLINA: DESENVOLVIMENTO ORIENTADO A TESTES
#DATA: 04/12/2024

# Faça uma função que recebe por parâmetro o tempo de duração de um processo em uma fábrica expressa em segundos e retorna também por parâmetro esse tempo em horas, minutos e segundos.

def tempo(x):
    if type(x) != int or x < 0:
        return Exception
    h = x // 3600
    m = (x % 3600) // 60
    s = x % 60
    return (h, m, s)

assert tempo(3600) == (1, 0, 0)
assert tempo(3666) == (1, 1, 6)
assert tempo(7200) == (2, 0, 0)
assert tempo(7405) == (2, 3, 25)
assert tempo(10860) == (3, 1, 0)

assert tempo(0) == (0, 0, 0)
assert tempo("x") == Exception
assert tempo(True) == Exception
assert tempo(-3600) == Exception

print("Todos os testes ok!")