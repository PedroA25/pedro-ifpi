#INSTITUTO FEDERAL DE EDUCAÇÃO, CIÊNCIA E TECNOLOGIA DO PIAUÍ
#CAMPUS TERESINA CENTRAL
#TÉCNICO EM DESENVOLVIMENTO DE SISTEMAS
#PROF.: OSIRES PIRES COELHO FILHO
#ALUNO: PEDRO AUGUSTO RODRIGUES MELO
#DISCIPLINA: DESENVOLVIMENTO ORIENTADO A TESTES
#DATA: 19/12/2024

# A prefeitura de uma cidade fez uma pesquisa entre os seus habitantes, coletando dados sobre o salário e número de filhos.
# Faça uma função que leia esses dados para um número não determinado de pessoas e retorne a média de
# salário da população, a média do número de filhos, o maior salário e o percentual
# de pessoas com salário até R$ 350,00.

def prefeitura(s, n):
    if len(s) != len(n):
        return Exception
    if any(isinstance(i, (bool, str, float)) or i < 0 for i in s):
        return Exception
    if any(isinstance(i, (bool, str, float)) or i < 0 for i in n):
        return Exception
    salario_baixo = sum(1 for i in s if i <= 350.0)

    media_salario = sum(s) / len(s)
    media_filhos = sum(n) / len(s)
    maior_salario = max(s)
    percentual = (salario_baixo / len(s)) * 100

    return (round(media_salario, 2), round(media_filhos, ), round(maior_salario, 2), round(percentual, 2))

assert prefeitura([500, 350, 200],[2, 1, 3]) == (350.0, 2.0, 500, 66.67)
assert prefeitura([100, 300, 400], [4, 2, 1]) == (266.67, 2, 400, 66.67)
assert prefeitura([0], [0]) == (0, 0, 0, 100)
assert prefeitura([5000, 0], [0, 0]) == (2500, 0, 5000, 50)

assert prefeitura([-4], [0]) == Exception
assert prefeitura([True], [0]) == Exception
assert prefeitura(["e"], [2]) == Exception
assert prefeitura([2.3], [3.4]) == Exception

print("Todos os testes ok.")
