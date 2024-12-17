# Faça uma função que recebe um valor inteiro e verifica se o valor é par ou ímpar. A função deve retornar um valor booleano.

def impar_par(x):
    if type(x) != int:
        return Exception
    if x % 2 == 0:
        return True
    else: 
        return False
    
assert impar_par(2) == True
assert impar_par(20) == True
assert impar_par(40) == True
assert impar_par(21) == False
assert impar_par(3) == False
assert impar_par(71) == False

assert impar_par(0) == True
assert impar_par(True) == Exception
assert impar_par(-4) == True
assert impar_par(-1) == False
assert impar_par("w") == Exception

print("Todos os testes ok.")