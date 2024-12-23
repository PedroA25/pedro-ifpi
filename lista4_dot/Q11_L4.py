#INSTITUTO FEDERAL DE EDUCAÇÃO, CIÊNCIA E TECNOLOGIA DO PIAUÍ
#CAMPUS TERESINA CENTRAL
#TÉCNICO EM DESENVOLVIMENTO DE SISTEMAS
#PROF.: OSIRES PIRES COELHO FILHO
#ALUNO: PEDRO AUGUSTO RODRIGUES MELO
#DISCIPLINA: DESENVOLVIMENTO ORIENTADO A TESTES
#DATA: 19/12/2024

# Faça uma função que recebe, por parâmetro, a altura e o sexo de uma pessoa e retorna o seu peso ideal.
# Para homens, calcular o peso ideal usando a fórmula peso ideal = 72.7 * altura - 58 e, 
# para mulheres, peso ideal = 62.1 * altura - 44.7.

def peso_ideal(a, s):
    if type(a) != float and type(a) != int:
        return Exception
    if a < 1 or a >= 3:
        return Exception
    if s not in [1, 2]:
        return Exception
    if s == 1:
        peso = (62.1 * a) - 44.70
        return round(peso, 2)
    elif s == 2:
        peso = (72.7 * a) - 58
        return round(peso, 2)
    
assert peso_ideal(1, 1) == 17.4
assert peso_ideal(1, 2) == 14.7
assert peso_ideal(1.7, 1) == 60.87
assert peso_ideal(1.7, 2) == 65.59

assert peso_ideal(23, 1) == Exception
assert peso_ideal("m", 1) == Exception
assert peso_ideal(True, 2) == Exception
assert peso_ideal(2, 4) == Exception

print("Todos os testes ok.")
