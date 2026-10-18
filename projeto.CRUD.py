# Inicialização das variáveis do sistema (sem listas)
cliente_cadastrado = False
nome = ""
cpf = ""
idade = ""
sexo = ""
especialidade = ""
profissional = ""
horario = ""
status_atendimento = ""

# Loop principal do menu
opcao = ""

while opcao != "5":
    print("\n=== CLÍNICA ODONTOLÓGICA - SISTEMA DE AGENDAMENTO ===")
    print("1. Cadastrar Agendamento (Create)")
    print("2. Consultar Agendamento (Read)")
    print("3. Atualizar Agendamento (Update)")
    print("4. Excluir Agendamento (Delete)")
    print("5. Sair")
    
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        if cliente_cadastrado:
            print("\nJá existe um agendamento ativo. Exclua ou atualize o atual.")
        else:
            print("\n--- CADASTRO DE CLIENTE ---")
            nome = input("Nome completo do cliente: ")
            cpf = input("CPF do cliente: ")
            idade = input("Idade: ")
            sexo = input("Sexo: ")
            
            print("\n--- ESPECIALIDADES DO DIA ---")
            print("1. Odontopediatria")
            print("2. Endodontia")
            print("3. Ortodontia")
            op_esp = input("Escolha a especialidade (1-3): ")
            
            if op_esp == "1":
                especialidade = "Odontopediatria"
                profissional = "Dra. Ana (Presente)"
                horario = "09:00"
            elif op_esp == "2":
                especialidade = "Endodontia"
                profissional = "Dr. Carlos (Presente)"
                horario = "14:00"
            elif op_esp == "3":
                especialidade = "Ortodontia"
                profissional = "Dra. Beatriz (Presente)"
                horario = "16:00"
            else:
                especialidade = "Clínico Geral"
                profissional = "Dr. João (Presente)"
                horario = "10:30"
                
            print("\n--- STATUS DO ATENDIMENTO ---")
            print("1. Normal")
            print("2. Urgente")
            op_status = input("Escolha a prioridade (1-2): ")
            
            if op_status == "2":
                status_atendimento = "URGENTE"
            else:
                status_atendimento = "Normal"
                
            cliente_cadastrado = True
            print("\nAgendamento realizado com sucesso!")

    elif opcao == "2":
        if not cliente_cadastrado:
            print("\nNenhum agendamento encontrado.")
        else:
            print("\n--- DADOS DO AGENDAMENTO ---")
            print(f"Nome: {nome}")
            print(f"CPF: {cpf}")
            print(f"Idade: {idade}")
            print(f"Sexo: {sexo}")
            print(f"Especialidade: {especialidade}")
            print(f"Profissional: {profissional}")
            print(f"Horário: {horario}")
            print(f"Status: {status_atendimento}")

    elif opcao == "3":
        if not cliente_cadastrado:
            print("\nNão há agendamento para atualizar.")
        else:
            print("\n--- ATUALIZAR DADOS ---")
            nome = input(f"Novo nome (atual: {nome}): ")
            idade = input(f"Nova idade (atual: {idade}): ")
            
            print("Status atual:", status_atendimento)
            novo_status = input("O atendimento agora é urgente? (s/n): ")
            if novo_status.lower() == "s":
                status_atendimento = "URGENTE"
            else:
                status_atendimento = "Normal"
                
            print("\nAgendamento atualizado com sucesso!")

    elif opcao == "4":
        if not cliente_cadastrado:
            print("\nNão há agendamento para excluir.")
        else:
            nome = ""
            cpf = ""
            idade = ""
            sexo = ""
            especialidade = ""
            profissional = ""
            horario = ""
            status_atendimento = ""
            cliente_cadastrado = False
            print("\nAgendamento excluído com sucesso!")

    elif opcao == "5":
        print("\nSaindo do sistema. Até logo!")

    else:
        print("\nOpção inválida! Escolha entre 1 e 5.")