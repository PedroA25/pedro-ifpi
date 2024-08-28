from datetime import datetime, date, timedelta

class ConsultaMedica:
    valor_consulta = 300
    valor_medico = 200
    
    def __init__(self, data_consulta, paciente, medico):
        self.data_consulta = datetime.strptime(data_consulta, "%d/%m/%Y").date()
        self.validar_data_consulta()
        self.data_retorno = None
        self.paciente = paciente
        self.medico = medico
        self.pago = False
        self.cancelado = False

    def validar_data_consulta(self):
        if self.data_consulta <= date.today() or self.data_consulta.weekday() in [5, 6]:
            raise ValueError("A data da consulta deve ser maior que a data atual e não pode cair em um final de semana.")

    def pagar_consulta(self):
        if not self.cancelado:
            self.pago = True
        else:
            raise ValueError("Consulta cancelada não pode ser paga.")

    def cancelar_consulta(self):
        if not self.pago:
            self.cancelado = True
        else:
            raise ValueError("Consulta paga não pode ser cancelada.")

    def agendar_retorno(self, data_retorno):
        if not self.pago:
            raise ValueError("Só é possível agendar retorno para consultas pagas.")
        data_retorno = datetime.strptime(data_retorno, "%d/%m/%Y").date()
        if data_retorno <= self.data_consulta or data_retorno > self.data_consulta + timedelta(days=30):
            raise ValueError("Data de retorno deve ser dentro de 30 dias após a consulta.")
        if data_retorno.weekday() in [5, 6]:
            raise ValueError("Data de retorno não pode cair em um final de semana.")
        self.data_retorno = data_retorno

consultas = []

def nova_consulta():
    data_consulta = input("Digite a data da consulta (dd/mm/aaaa): ")
    paciente = input("Digite o nome do paciente: ")
    medico = input("Digite o nome do médico: ")
    try:
        consulta = ConsultaMedica(data_consulta, paciente, medico)
        consultas.append(consulta)
        print("Consulta agendada!")
    except ValueError as e:
        print(f"Erro: {e}")

def pagar_consulta():
    paciente = input("Digite o nome do paciente: ")
    consulta = encontrar_consulta(paciente)
    if consulta:
        try:
            consulta.pagar_consulta()
            print("Consulta paga!")
        except ValueError as e:
            print(f"Erro: {e}")

def cancelar_consulta():
    paciente = input("Digite o nome do paciente: ")
    consulta = encontrar_consulta(paciente)
    if consulta:
        try:
            consulta.cancelar_consulta()
            print("Consulta cancelada!")
        except ValueError as e:
            print(f"Erro: {e}")

def agendar_retorno():
    paciente = input("Digite o nome do paciente: ")
    consulta = encontrar_consulta(paciente)
    if consulta:
        data_retorno = input("Digite a data do retorno (dd/mm/aaaa): ")
        try:
            consulta.agendar_retorno(data_retorno)
            print("Retorno agendado!")
        except ValueError as e:
            print(f"Erro: {e}")

def encontrar_consulta(paciente):
    for consulta in consultas:
        if consulta.paciente == paciente:
            return consulta
    print("Consulta não encontrada.")
    return None

def relatorio_consultas_realizadas_mes():
    medico = input("Digite o nome do médico: ")
    mes = int(input("Digite o mês (1-12): "))
    ano = int(input("Digite o ano (aaaa): "))
    consultas_mes = [c for c in consultas if c.medico == medico and c.data_consulta.month == mes and c.data_consulta.year == ano and c.pago]
    print(f"Consultas realizadas por {medico} em {mes}/{ano}: {len(consultas_mes)}")

def relatorio_faturamento_clinica_mes():
    mes = int(input("Digite o mês (1-12): "))
    ano = int(input("Digite o ano (aaaa): "))
    consultas_mes = [c for c in consultas if c.data_consulta.month == mes and c.data_consulta.year == ano and c.pago]
    faturamento = len(consultas_mes) * (ConsultaMedica.valor_consulta - ConsultaMedica.valor_medico)
    print(f"Faturamento da clínica em {mes}/{ano}: R${faturamento}")

def menu():
    while True:
        print("\nMenu:")
        print("1 - Nova consulta (agendamento)")
        print("2 - Pagar consulta")
        print("3 - Cancelar consulta")
        print("4 - Agendar retorno")
        print("5 - Relatório de consultas realizadas no mês por médico")
        print("6 - Relatório de faturamento da clínica por mês")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            nova_consulta()
        elif opcao == '2':
            pagar_consulta()
        elif opcao == '3':
            cancelar_consulta()
        elif opcao == '4':
            agendar_retorno()
        elif opcao == '5':
            relatorio_consultas_realizadas_mes()
        elif opcao == '6':
            relatorio_faturamento_clinica_mes()
        elif opcao == '0':
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
