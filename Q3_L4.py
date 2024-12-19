#INSTITUTO FEDERAL DE EDUCAÇÃO, CIÊNCIA E TECNOLOGIA DO PIAUÍ
#CAMPUS TERESINA CENTRAL
#TÉCNICO EM DESENVOLVIMENTO DE SISTEMAS
#PROF.: OSIRES PIRES COELHO FILHO
#ALUNO: PEDRO AUGUSTO RODRIGUES MELO
#DISCIPLINA: DESENVOLVIMENTO ORIENTADO A TESTES
#DATA: 03/12/2024


# Faça uma função que recebe por parâmetro um valor inteiro e positivo e retorna o valor lógico Verdadeiro caso o valor seja primo e Falso em caso contrário.

def primo(x):
    primo = True
    if type(x) != int or x <= 0:
        return Exception
    if x == 1:
        primo = False
    for i in range(2, x):
        if x % i == 0:
            primo = False
    return primo

assert primo(10) == False
assert primo(24) == False
assert primo(1250) == False
assert primo(19) == True
assert primo(97) == True
assert primo(17) == True
assert primo(1) == False

assert primo(-3) == Exception
assert primo("x") == Exception
assert primo(True) == Exception
assert primo(0) == Exception

print("Todos os testes ok!")