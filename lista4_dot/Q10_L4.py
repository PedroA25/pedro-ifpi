#INSTITUTO FEDERAL DE EDUCAÇÃO, CIÊNCIA E TECNOLOGIA DO PIAUÍ
#CAMPUS TERESINA CENTRAL
#TÉCNICO EM DESENVOLVIMENTO DE SISTEMAS
#PROF.: OSIRES PIRES COELHO FILHO
#ALUNO: PEDRO AUGUSTO RODRIGUES MELO
#DISCIPLINA: DESENVOLVIMENTO ORIENTADO A TESTES
#DATA: 19/12/2024

# Faça uma função que recebe a média final de um aluno por parâmetro e retorna o seu conceito, conforme a tabela

def media(x):
    if type(x) != int and type(x) != float:
        return Exception
    if x < 0 or x > 10:
        return Exception
    if 0 <= x < 5:
        return "D"
    elif 5 <= x < 7:
        return "C"
    elif 7 <= x < 9:
        return "B"
    elif 9 <= x <= 10:
        return "A"
    
assert media(2.5) == "D"
assert media(5.5) == "C"
assert media(7) == "B"
assert media(10) == "A"

assert media(11) == Exception
assert media(-1) == Exception
assert media(True) == Exception
assert media(None) == Exception
assert media("w") == Exception

print("Todos os testes ok.")