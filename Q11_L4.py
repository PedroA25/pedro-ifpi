# Faça uma função que recebe, por parâmetro, a altura e o sexo de uma pessoa e retorna o seu peso ideal.
# Para homens, calcular o peso ideal usando a fórmula peso ideal = 72.7 * altura - 58 e, 
# para mulheres, peso ideal = 62.1 * altura - 44.7.

def peso_ideal(a, s):
    if type(a) != float and type(a) != int:
        return Exception
    if a < 1:
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


print("Todos os testes ok.")
