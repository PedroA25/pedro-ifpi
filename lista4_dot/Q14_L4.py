#INSTITUTO FEDERAL DE EDUCAÇÃO, CIÊNCIA E TECNOLOGIA DO PIAUÍ
#CAMPUS TERESINA CENTRAL
#TÉCNICO EM DESENVOLVIMENTO DE SISTEMAS
#PROF.: OSIRES PIRES COELHO FILHO
#ALUNO: PEDRO AUGUSTO RODRIGUES MELO
#DISCIPLINA: DESENVOLVIMENTO ORIENTADO A TESTES
#DATA: 19/12/2024

# Escreva uma função que recebes 3 valores reais X, Y e Z e que verifique se esses valores podem ser os comprimentos dos lados de um 
# triângulo e, neste caso, retornar qual o tipo de triângulo formado. Para que X, Y e Z formem um triângulo é necessário que
# a seguinte propriedade seja satisfeita: o comprimento de cada lado de um triângulo é menor do que a soma do comprimento dos outros
#dois lados. O procedimento deve identificar o tipo de triângulo formado observando as seguintes definições:

# o Triângulo Equilátero: os comprimentos dos 3 lados são iguais.
# o Triângulo Isósceles: os comprimentos de 2 lados são iguais.
# o Triângulo Escaleno: os comprimentos dos 3 lados são diferentes.

def triangulo(X, Y, Z):
    if type(X) != int and type(X) != float:
        return Exception
    if type(Y) != int and type(Y) != float:
        return Exception
    if type(Z) != int and type(Z) != float:
        return Exception
    if X + Y <= Z or X + Z <=Y or Y + Z <= X:
        return Exception
    if X == Y == Z:
        return "Triângulo Equilátero"
    elif X == Y or X == Z or Y == Z:
        return "Triângulo Isósceles"
    elif X != Y != Z:
        return "Triângulo Escaleno"

print("Todos os testes ok.")