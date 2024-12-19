#INSTITUTO FEDERAL DE EDUCAÇÃO, CIÊNCIA E TECNOLOGIA DO PIAUÍ
#CAMPUS TERESINA CENTRAL
#TÉCNICO EM DESENVOLVIMENTO DE SISTEMAS
#PROF.: OSIRES PIRES COELHO FILHO
#ALUNO: PEDRO AUGUSTO RODRIGUES MELO
#DISCIPLINA: DESENVOLVIMENTO ORIENTADO A TESTES
#DATA: 19/12/2024

# Faça uma função que recebe um valor inteiro e verifica se o valor é positivo ou negativo. A função deve retornar um valor booleano.

def posi_nega(x):
    if type(x) != int or x == 0:
        return Exception
    if x > 0:
        return True
    elif x < 0:
        return False
    
assert posi_nega(4) == True
assert posi_nega(56) == True
assert posi_nega(40) == True
assert posi_nega(-9) == False
assert posi_nega(-45) == False
assert posi_nega(-1) == False

assert posi_nega(0) == Exception
assert posi_nega(True) == Exception
assert posi_nega(2.3) == Exception
assert posi_nega(None) == Exception

print("Todos os testes ok.")