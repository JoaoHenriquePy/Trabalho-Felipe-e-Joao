op = 999

usuarios = [["admin", "123", "ADM"], ["cliente", "456", "CLIENTE"]]
rebanho = []
historico_compras = []
estoque = [
    ["Queijo Coalho", 120.0, 42.90],
    ["Queijo Manteiga", 80.0, 48.50],
    ["Leitão", 25.0, 180.0],
    ["Leite (Litros)", 0.0, 3.50]
]

usuario_logado = ""  
tipo_logado = ""      

while op != 3:
    print("\n------- MENU PRINCIPAL -------")
    print(" 1. Fazer Login")
    print(" 2. Cadastrar Novo Usuário")        
    print(" 3. Sair do Sistema")
    print("------------------------------")
    op = int(input("Digite a opção desejada: "))

    if op == 1:
        usuario_digitado = input("Digite seu nome de usuário: ")
        senha = input("Digite sua senha: ")
       
        encontrado = False
        i = 0
        while i < len(usuarios):
            nome_usuario, senha_usuario, tipo_usuario = usuarios[i]
            if nome_usuario == usuario_digitado and senha_usuario == senha:
                usuario_logado = nome_usuario
                tipo_logado = tipo_usuario
                encontrado = True
                print(f"\nBem-vindo, {usuario_logado}! Perfil: {tipo_logado}")
                break
            i = i + 1
       
        if not encontrado:
            print("\n Senha ou nome de usuário inválido!")
        else:
            continua_adm = "sim"
            while tipo_logado == "ADM" and continua_adm == "sim":
                print("\n--------- PAINEL DO ADMINISTRADOR ---------")
                print("Opções: 1-Cadastrar | 2-Buscar | 3-Atualizar | 4-Remover")
                print("5-Relatório | 6-Produção | 7-Sair do Painel")
                proxima = input("Escolha o que deseja fazer: ").lower()

                if proxima in ["cadastrar", "1"]:
                    print("\nCadastro de Animal (Tipos permitidos: Bovino, Caprino, Ovino, Suino)")
                    tipo = input("Tipo de animal: ").lower()
                    
                    while tipo not in ["bovino", "caprino", "ovino", "suino"]:
                        print("Tipo inválido! Escolha entre Bovino, Caprino, Ovino ou Suíno.")
                        tipo = input("Tipo de animal: ").lower()
                        
                    identificacao = input("Identificação (Ex: Brinco, chip ou ID): ")
                    status = input("Status do animal (Ex: Venda, Engorda, Tratamento): ")
                    animal = [tipo, identificacao, status]
                    rebanho.append(animal)
                    print(f"Animal {identificacao} cadastrado!")

                elif proxima in ["buscar", "2"]:
                    buscar = input("Qual identificação (ID/Brinco) você está procurando? ").lower()
                    encontrado_busca = False
                    i = 0
                    while i < len(rebanho):
                        if rebanho[i][1].lower() == buscar:
                            print(f"\n Tipo: {rebanho[i][0]} | ID: {rebanho[i][1]} | Status: {rebanho[i][2]}")
                            encontrado_busca = True
                        i = i + 1
                    if not encontrado_busca:
                        print("Animal não encontrado.")

                elif proxima in ["atualizar", "3"]:
                    buscar = input("Informe a identificação do animal que deseja atualizar: ").lower()
                    encontrado_atualizar = False
                    i = 0
                    while i < len(rebanho):
                        if rebanho[i][1].lower() == buscar:
                            print(f"Animal localizado! Status atual: {rebanho[i][2]}")
                            novo_status = input("Novo status do animal: ")
                            rebanho[i][2] = novo_status
                            print("Status atualizado com sucesso!")
                            encontrado_atualizar = True
                            break  
                        i = i + 1  
                        
                    if not encontrado_atualizar:
                        print("Nenhum animal foi encontrado com essa identificação.")

                elif proxima in ["remover", "4"]:
                    remover = input("Qual identificação do animal quer remover? ").lower()
                    i = 0
                    removido = False
                    while i < len(rebanho):
                        if rebanho[i][1].lower() == remover:
                            del rebanho[i]
                            print("Animal removido do sistema!")
                            removido = True
                            break
                        i = i + 1
                    if not removido:
                        print("Animal não encontrado.")

                elif proxima in ["relatorio", "5"]:
                    print("\n RELATÓRIO DE REBANHO E VENDAS ")
                    bovino = 0; caprino = 0; ovino = 0; suino = 0; disponiveis_venda = 0
                    i = 0
                    while i < len(rebanho):
                        tipo_animal = rebanho[i][0].lower()
                        status_animal = rebanho[i][2].lower()
                        
                        if tipo_animal == "bovino": bovino += 1
                        elif tipo_animal == "caprino": caprino += 1
                        elif tipo_animal == "ovino": ovino += 1
                        elif tipo_animal == "suino": suino += 1
                        
                        if status_animal in ["venda", "disponivel para venda", "engorda"]:
                            disponiveis_venda += 1
                        i += 1

                    print(f"Bovinos: {bovino}, Caprinos: {caprino}, Ovinos: {ovino}, Suínos: {suino}")
                    print(f"Total de animais no rebanho: {len(rebanho)}")
                    print(f"Animais disponíveis para venda: {disponiveis_venda}")

                elif proxima in ["producao", "6"]:
                    print("\n--- ATUALIZAR PRODUÇÃO/ESTOQUE ---")
                    nome_prod_atualizar = input("Digite o nome exato do produto: ")
                    achou_produto = False
                    ponteiro = 0
                    
                    while ponteiro < len(estoque):
                        if estoque[ponteiro][0].lower() == nome_prod_atualizar.lower():
                            quantidade_nova = float(input(f"Quantidade de '{estoque[ponteiro][0]}' a ser adicionada: "))
                            estoque[ponteiro][1] += quantidade_nova
                            print("Estoque atualizado com sucesso!")
                            achou_produto = True
                            break
                        ponteiro += 1
                    
                    if not achou_produto:
                        print("Produto não cadastrado no estoque inicial.")

                elif proxima in ["sair do painel", "7"]:
                    continua_adm = "nao"
                    print("Saindo do painel administrativo...")

            continua_cliente = "sim"
            while tipo_logado == "CLIENTE" and continua_cliente == "sim":
                print("\n--------- MENU CLIENTE ---------")
                print("1. Ver estoque e comprar")
                print("2. Histórico de compras")
                print("3. Agendar retirada de produtos")
                print("4. Sair do Painel")
                escolha = input("Escolha uma opção: ")

                if escolha == "1":
                    print("\n=== ESTOQUE ATUAL ===")
                    i = 0
                    while i < len(estoque):
                        nome_prod, qtd_prod, preco_prod = estoque[i]
                        print(f"{i+1} - {nome_prod} | Disponível: {qtd_prod} | Preço: R${preco_prod:.2f}")
                        i = i + 1
                    
                    num = int(input("\nDigite o NÚMERO do produto que deseja comprar: ")) - 1
                    
                    if 0 <= num < len(estoque):
                        nome_prod, qtd_disponivel, preco_prod = estoque[num]
                        qtd_desejada = float(input(f"Quantos '{nome_prod}' você deseja? "))
                        
                        if qtd_desejada <= qtd_disponivel:
                            valor_total = qtd_desejada * preco_prod
                            print(f"Valor total do pedido: R$ {valor_total:.2f}")
                            confirma = input("Confirmar compra? (s/n): ").lower()
                            
                            if confirma == "s":
                                estoque[num][1] -= qtd_desejada
                                historico_compras.append([usuario_logado, nome_prod, qtd_desejada, valor_total, "Pendente"])
                                print("Compra realizada com sucesso!")
                        else:
                            print("Quantidade insuficiente em estoque!")
                    else:
                        print("Opção de produto inválida.")

                elif escolha == "2":
                    print("\n--- MEU HISTÓRICO DE COMPRAS ---")
                    total_gasto = 0.0
                    tem_compra = False
                    
                    contagem_produtos = [
                        ["Queijo Coalho", 0], ["Queijo Manteiga", 0],
                        ["Leitão", 0], ["Leite (Litros)", 0]
                    ]

                    i = 0
                    while i < len(historico_compras):
                        dono_compra, item, qtd, gasto, status_frete = historico_compras[i]
                        
                        if dono_compra == usuario_logado:
                            print(f"Status Retirada: {status_frete} | {item} | Qtd: {qtd} | Total: R$ {gasto:.2f}")
                            total_gasto += gasto
                            tem_compra = True

                            c = 0
                            while c < len(contagem_produtos):
                                if contagem_produtos[c][0] == item:
                                    contagem_produtos[c][1] += 1
                                c += 1
                        i += 1

                    if not tem_compra:
                        print("Você ainda não realizou compras.")
                    else:
                        print(f"\nTotal gasto acumulado: R$ {total_gasto:.2f}")

                        mais_comprado_nome = ""
                        maior_quantidade = 0
                        m = 0
                        while m < len(contagem_produtos):
                            if contagem_produtos[m][1] > maior_quantidade:
                                maior_quantidade = contagem_produtos[m][1]
                                mais_comprado_nome = contagem_produtos[m][0]
                            m += 1
                        
                        if maior_quantidade > 0:
                            print(f"Seu produto mais frequente: {mais_comprado_nome}")

                elif escolha == "3":
                    data_escolhida = input("Digite a data para retirada (Ex: 20/05): ")
                    hora_escolhida = input("Digite o horário (Ex: 15:00): ") 
                    p = 0
                    while p < len(historico_compras):
                        if historico_compras[p][0] == usuario_logado and historico_compras[p][4] == "Pendente":
                            historico_compras[p][4] = f"{data_escolhida} às {hora_escolhida}"
                        p = p + 1
                    print("Retirada agendada para os pedidos pendentes!")

                elif escolha == "4":
                    continua_cliente = "nao"
                    print("Saindo do painel do cliente...")

    elif op == 2:
        print("\n--- CADASTRO DE NOVO USUÁRIO ---")
        novo_usuario = input("Digite o nome do novo usuário: ")
        nova_senha = input("Digite a senha: ")
        tipo_novo = input("Tipo de permissão (Digite ADM ou CLIENTE): ").upper()

        while tipo_novo not in ["ADM", "CLIENTE"]:
            print("Permissão inválida. Escolha apenas entre ADM ou CLIENTE.")
            tipo_novo = input("Tipo de permissão (ADM ou CLIENTE): ").upper()   
            
        usuarios.append([novo_usuario, nova_senha, tipo_novo])
        print("Novo usuário cadastrado!")

    elif op == 3:
        print("\nMenu encerrado e sistema fechado com sucesso.")