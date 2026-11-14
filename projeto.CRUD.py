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

# Versão mais atualizada com mais funcionalidades utilizando listas e dicionários:

agendamentos = []

# Lista fixa com as opções de atendimento
opcoes_esp = [
    {"esp": "Odontopediatria", "prof": "Dra. Ana (Presente)", "horario": "09:00"},
    {"esp": "Endodontia", "prof": "Dr. Carlos (Presente)", "horario": "14:00"},
    {"esp": "Ortodontia", "prof": "Dra. Beatriz (Presente)", "horario": "16:00"},
    {"esp": "Clínico Geral", "prof": "Dr. João (Presente)", "horario": "10:30"}
]

while True:
    print("\n=== CLÍNICA ODONTOLÓGICA ===")
    print("1. Cadastrar Agendamento")
    print("2. Listar Agendamentos")
    print("3. Atualizar Agendamento")
    print("4. Excluir Agendamento")
    print("5. Sair")
    
    opcao = input("Escolha uma opção (1-5): ")

    if opcao == "1":
        print("\n--- NOVO CADASTRO ---")
        nome = input("Nome completo: ")
        cpf = input("CPF: ")
        idade = input("Idade: ")
        sexo = input("Sexo: ")
        
        # Laço para garantir escolha válida da especialidade
        while True:
            print("\nEspecialidades disponíveis:")
            for i, o in enumerate(opcoes_esp):
                print(f"{i+1}. {o['esp']} ({o['prof']} - {o['horario']})")
            
            escolha = input("Escolha a especialidade (1-4): ")
            if escolha in ["1", "2", "3", "4"]:
                obj = opcoes_esp[int(escolha) - 1]
                break
            print("[Erro] Opção inválida! Escolha entre 1 e 4.")

        # Laço para garantir escolha válida do status
        while True:
            st = input("Status do atendimento - 1. Normal | 2. Urgente: ")
            if st in ["1", "2"]:
                status = "URGENTE" if st == "2" else "Normal"
                break
            print("[Erro] Digite 1 ou 2.")

        # Adiciona o novo dicionário na lista de agendamentos (permite múltiplos pacientes)
        agendamentos.append({
            "nome": nome, 
            "cpf": cpf, 
            "idade": idade, 
            "sexo": sexo,
            "especialidade": obj["esp"], 
            "profissional": obj["prof"],
            "horario": obj["horario"], 
            "status": status
        })
        print("\nAgendamento realizado com sucesso!")

    elif opcao == "2":
        if not agendamentos:
            print("\nNenhum agendamento encontrado no sistema.")
        else:
            print("\n--- LISTA DE AGENDAMENTOS ---")
            for i, ag in enumerate(agendamentos):
                print(f"\n[{i+1}] Paciente: {ag['nome']}")
                print(f"    CPF: {ag['cpf']} | Idade: {ag['idade']} | Sexo: {ag['sexo']}")
                print(f"    Especialidade: {ag['especialidade']}")
                print(f"    Profissional: {ag['profissional']}")
                print(f"    Horário: {ag['horario']}")
                print(f"    Status: {ag['status']}")

    elif opcao == "3" or opcao == "4":
        if not agendamentos:
            print("\nNão há agendamentos cadastrados.")
            continue
            
        cpf_busca = input(f"Digite o CPF do cliente para {'atualizar' if opcao=='3' else 'excluir'}: ")
        encontrado = False
        
        for i, ag in enumerate(agendamentos):
            if ag["cpf"] == cpf_busca:
                encontrado = True
                if opcao == "3":
                    ag["nome"] = input(f"Novo nome ({ag['nome']}): ") or ag["nome"]
                    ag["idade"] = input(f"Nova idade ({ag['idade']}): ") or ag["idade"]
                    resp = input("O atendimento é urgente? (s/n): ").lower()
                    if resp in ["s", "n"]:
                        ag["status"] = "URGENTE" if resp == "s" else "Normal"
                    print("\nAgendamento atualizado com sucesso!")
                else:
                    agendamentos.pop(i)
                    print("\nAgendamento excluído com sucesso!")
                break
        
        if not encontrado:
            print("\nCliente não encontrado com esse CPF.")

    elif opcao == "5":
        print("\nSaindo do sistema. Até logo!")
        break
    else:
        print("\nOpção inválida! Escolha entre 1 e 5.")



