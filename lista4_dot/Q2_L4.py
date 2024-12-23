#INSTITUTO FEDERAL DE EDUCAÇÃO, CIÊNCIA E TECNOLOGIA DO PIAUÍ
#CAMPUS TERESINA CENTRAL
#TÉCNICO EM DESENVOLVIMENTO DE SISTEMAS
#PROF.: OSIRES PIRES COELHO FILHO
#ALUNO: PEDRO AUGUSTO RODRIGUES MELO
#DISCIPLINA: DESENVOLVIMENTO ORIENTADO A TESTES
#DATA: 03/12/2024

# Escreva uma função que recebe as 3 notas de um aluno por parâmetro e uma letra. Se a letra for A o procedimento calcula a média aritmética das notas do
# aluno, se for P, a sua média ponderada (pesos: 5, 3 e 2). A função deve retornar a média calculada.   

def medias(x, y, z, m):
    if type(x) != int and type(x) != float:
        return Exception
    if  type(y) != int and type(y) != float:
        return Exception
    if type(z) != int and type(z) != float:
        return Exception
    if x > 10 or x < 0:
        return Exception
    if y > 10 or y < 0:
        return Exception
    if z > 10 or z < 0:
        return Exception     
    if m == 'A' or m == 'a':
        aritmetica = (x + y + z)/ 3
        return round(aritmetica, 2)
    elif m == 'P' or m == 'p':
        ponderada = ((x*5)+(y*3)+(z*2))/(5+3+2)
        return round(ponderada, 2)
    if m not in ['A', 'P', 'a', 'p']:
        return Exception


assert medias(2, 3, 4, "A") == 3.0
assert medias(2, 3, 4, "P") == 2.7
assert medias(30.5, 23, 5.5, "a") == Exception
assert medias(0, 0, 0, 'p') == 0.0
assert medias(5, 6, -4, 'p') == Exception


assert medias(2, 3, 4, "M") == Exception
assert medias('a', 4, 'f', 0) == Exception
assert medias(2, 4, 5, True) == Exception

print("Todos os testes ok!")
