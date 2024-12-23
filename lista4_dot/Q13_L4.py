#INSTITUTO FEDERAL DE EDUCAÇÃO, CIÊNCIA E TECNOLOGIA DO PIAUÍ
#CAMPUS TERESINA CENTRAL
#TÉCNICO EM DESENVOLVIMENTO DE SISTEMAS
#PROF.: OSIRES PIRES COELHO FILHO
#ALUNO: PEDRO AUGUSTO RODRIGUES MELO
#DISCIPLINA: DESENVOLVIMENTO ORIENTADO A TESTES
#DATA: 19/12/2024

# Faça uma função que recebe, por parâmetro, a hora de inicio e a hora de término de um jogo,
# ambas subdivididas em 2 valores distintos: horas e minutos. O procedimento deve retornar, também por parâmetro, a duração do jogo em
# horas e minutos, considerando que o tempo máximo de duração de um jogo é 
# de 24 horas e que o jogo pode começar em um dia e terminar no outro.

def jogo(hi, mi, hf, mf):
    if type(hi) != int or type(mi) != int or type(hf) != int or type(mf) != int:
        return Exception
    if hi < 0 or mi < 0 or hf < 0 or mf < 0:
        return Exception
    if hi > 24 or mi > 59 or hf > 24 or mf > 59:
        return Exception
    inicio = (hi * 60) + mi
    final #INSTITUTO FEDERAL DE EDUCAÇÃO, CIÊNCIA E TECNOLOGIA DO PIAUÍ
#CAMPUS TERESINA CENTRAL
#TÉCNICO EM DESENVOLVIMENTO DE SISTEMAS
#PROF.: OSIRES PIRES COELHO FILHO
#ALUNO: PEDRO AUGUSTO RODRIGUES MELO
#DISCIPLINA: DESENVOLVIMENTO ORIENTADO A TESTES
#DATA: 19/12/2024

# Faça uma função que recebe, por parâmetro, a hora de inicio e a hora de término de um jogo,
# ambas subdivididas em 2 valores distintos: horas e minutos. O procedimento deve retornar, também por parâmetro, a duração do jogo em
# horas e minutos, considerando que o tempo máximo de duração de um jogo é 
# de 24 horas e que o jogo pode começar em um dia e terminar no outro.

def jogo(hi, mi, hf, mf):
    if type(hi) != int or type(mi) != int or type(hf) != int or type(mf) != int:
        return Exception
    if hi < 0 or mi < 0 or hf < 0 or mf < 0:
        return Exception
    if hi > 23 or mi > 59 or hf > 23 or mf > 59:
        return Exception
    inicio = (hi * 60) + mi
    final = (hf * 60) + mf
    if final <= inicio:
        final += 24 * 60
    d = final - inicio
    h = d // 60
    m = d % 60
    return h, m

assert jogo(10, 0, 12, 0) == (2, 0)
assert jogo(22, 30, 1, 30) == (3, 0)
assert jogo(0, 0, 0, 0) == (24, 0)
assert jogo(14, 45, 16, 15) == (1, 30)

assert jogo(23, 0, "w", 0) == Exception
assert jogo(True, 0, 0, 0) == Exception
assert jogo(20.3, 3, 2, 3) == Exception
assert jogo(-4, 0, -3, 4) == Exception

print("Todos os testes ok")= (hf * 60) + mf
    if final <= inicio:
        final += 24 * 60
    d = final - inicio
    h = d // 60
    m = d % 60
    return h, m


print("Todos os testes ok")