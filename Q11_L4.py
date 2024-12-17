# Faça uma função que recebe, por parâmetro, a altura e o sexo de uma pessoa e retorna o seu peso ideal.
# Para homens, calcular o peso ideal usando a fórmula peso ideal = 72.7 * altura - 58 e, 
# para mulheres, peso ideal = 62.1 * altura - 44.7.

def peso_ideal(a, s):
    if type(a) != float and type(a) != int:
        return Exception
    if s not in [1, 2] or a < 0:
        return Exception
    if s == 1:
        return round(62.1 * a - 44.70, 2)
    elif s == 2:
        return round(72.7 * a - 58, 2)
    
assert peso_ideal(1, 1) == 17.4
assert peso_ideal(1, 2) == 14.7


print("Todos os testes ok.")
print(peso_ideal(1, 2))