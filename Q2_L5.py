#INSTITUTO FEDERAL DE EDUCAÇÃO, CIÊNCIA E TECNOLOGIA DO PIAUÍ
#CAMPUS TERESINA CENTRAL
#TÉCNICO EM DESENVOLVIMENTO DE SISTEMAS
#PROF.: OSIRES PIRES COELHO FILHO
#ALUNO: PEDRO AUGUSTO RODRIGUES MELO
#DISCIPLINA: DESENVOLVIMENTO ORIENTADO A TESTES
#DATA: 07/01/2025

# Escreva uma função que recebe uma lista com n números inteiros, conta e imprime
# o número de vezes que cada número ocorre na sequência.

def ocorrencias(lista):
    if len(lista) == 0:
        return Exception
    for i in lista:
        if type(i) != int:
            return Exception
    d = {}
    for i in lista:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
       
    return d

assert ocorrencias([2, 2]) == {2:2}
assert ocorrencias([3, 3, 4, 5, 5, 5]) == {3:2, 4:1, 5: 3}
assert ocorrencias([3, 3, 5, 6, 7, 7, 8, 8]) == {3:2, 5:1, 6:1, 7:2, 8:2}

assert ocorrencias([3, "w", 4, 4, 4, 5]) == Exception
assert ocorrencias([]) == Exception
assert ocorrencias([2.5, 3, 3, 4]) == Exception
assert ocorrencias([True, 2, 3]) == Exception

print("Todos os testes ok")