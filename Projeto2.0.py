from InquirerPy import inquirer

opcao_menu_principal = "999"

rebanho = []
historico_compras = []

usuario_logado = ""
tipo_logado = ""

usuarios = [
    {"usuario": "rene", "senha": "123", "perfil": "ADM"},
    {"usuario": "cliente", "senha": "123", "perfil": "CLIENTE"}
]

estoque = [
    {"nome": "Queijo Coalho", "quantidade": 120.0, "preco": 42.90},
    {"nome": "Leite", "quantidade": 50.0, "preco": 3.50},
    {"nome": "Carne Bovina", "quantidade": 200.0, "preco": 25.00},
    {"nome": "Carne Suína", "quantidade": 150.0, "preco": 20.00},
    {"nome": "Carne Caprina", "quantidade": 100.0, "preco": 30.00}
]

while opcao_menu_principal != "3. Sair do Sistema":
    print("\n------- MENU PRINCIPAL -------")
    
    opcao_menu_principal = inquirer.select(
        message="Selecione a opção desejada:",
        choices=[
            "1. Fazer Login",
            "2. Cadastrar Novo Usuário",
            "3. Sair do Sistema"
        ]
    ).execute()

    if opcao_menu_principal == "1. Fazer Login":
        usuario_digitado = input("Digite seu nome de usuário: ")
        senha_digitada = input("Digite sua senha: ")
        login_sucesso = False

        indice_usuario = 0
        while indice_usuario < len(usuarios):
            nome_usuario = usuarios[indice_usuario]["usuario"]
            senha_usuario = usuarios[indice_usuario]["senha"]
            tipo_usuario = usuarios[indice_usuario]["perfil"]

            if nome_usuario == usuario_digitado:
                if senha_usuario == senha_digitada:
                    usuario_logado = nome_usuario
                    tipo_logado = tipo_usuario
                    login_sucesso = True
                    print("\nBem-vindo,", usuario_logado, "! Perfil:", tipo_logado)

            indice_usuario = indice_usuario + 1
            
        if login_sucesso == False:
            print("\nSenha ou nome de usuário inválido!")
        else:
            while tipo_logado == "ADM":
                print("\n--------- PAINEL DO ADMINISTRADOR ---------")
                
                escolha_administrador = inquirer.select(
                    message="Escolha uma opção:",
                    choices=[
                        "1 - Cadastrar Animal",
                        "2 - Buscar Animal",
                        "3 - Atualizar Animal",
                        "4 - Remover Animal",
                        "5 - Relatório",
                        "6 - Produção",
                        "7 - Consultar Vendas",
                        "8 - Sair"
                    ]
                ).execute()

                if escolha_administrador == "1 - Cadastrar Animal":
                    tipo_animal = inquirer.select(
                        message="Selecione o tipo do animal:",
                        choices=["Bovino", "Caprino", "Ovino", "Suíno"]
                    ).execute().lower()
                    
                    # Mensagem com os exemplos solicitados inserida aqui:
                    print("\nExemplos de identificação: Brinco 102, Mimosa, ID-05")
                    identificacao_animal = input("Digite a identificação do animal: ")
                    status_animal = input("Digite o status do animal: ")
                    
                    dados_animal = {"tipo": tipo_animal, "identificacao": identificacao_animal, "status": status_animal}
                    rebanho.append(dados_animal)
                    print("Animal cadastrado com sucesso!")

                elif escolha_administrador == "2 - Buscar Animal":
                    busca_animal = input("Digite a identificação do animal: ").lower()
                    animal_encontrado = False

                    indice_animal = 0
                    while indice_animal < len(rebanho):
                        identificacao_atual = rebanho[indice_animal]["identificacao"].lower()
                        if identificacao_atual == busca_animal:
                            print("\nAnimal encontrado!")
                            print("Tipo:", rebanho[indice_animal]["tipo"])
                            print("Identificação:", rebanho[indice_animal]["identificacao"])
                            print("Status:", rebanho[indice_animal]["status"])
                            animal_encontrado = True

                        indice_animal = indice_animal + 1
                    if animal_encontrado == False:
                        print("Animal não encontrado!")

                elif escolha_administrador == "3 - Atualizar Animal":
                    busca_animal = input("Digite a identificação do animal: ").lower()
                    animal_atualizado = False

                    indice_animal = 0
                    while indice_animal < len(rebanho):
                        identificacao_atual = rebanho[indice_animal]["identificacao"].lower()
                        if identificacao_atual == busca_animal:
                            print("Animal encontrado!")
                            print("Status atual:", rebanho[indice_animal]["status"])
                            novo_status = input("Digite o novo status: ")
                            rebanho[indice_animal]["status"] = novo_status
                            animal_atualizado = True
                            print("Status updated com sucesso!")

                        indice_animal = indice_animal + 1
                    if animal_atualizado == False:
                        print("Animal não encontrado!")

                elif escolha_administrador == "4 - Remover Animal":
                    remover_animal = input("Digite a identificação do animal: ").lower()
                    animal_removido = False

                    indice_animal = 0
                    while indice_animal < len(rebanho):
                        identificacao_atual = rebanho[indice_animal]["identificacao"].lower()
                        if identificacao_atual == remover_animal:
                            del rebanho[indice_animal]
                            animal_removido = True
                            print("Animal removido com sucesso!")
                            break

                        indice_animal = indice_animal + 1
                    if animal_removido == False:
                        print("Animal não encontrado!")

                elif escolha_administrador == "5 - Relatório":
                    quantidade_bovinos = 0
                    quantidade_caprinos = 0
                    quantidade_ovinos = 0
                    quantidade_suinos = 0
                    animais_disponiveis = 0

                    indice_animal = 0
                    while indice_animal < len(rebanho):
                        tipo_atual = rebanho[indice_animal]["tipo"].lower()
                        status_atual = rebanho[indice_animal]["status"].lower()

                        if tipo_atual == "bovino":
                            quantidade_bovinos = quantidade_bovinos + 1
                        elif tipo_atual == "caprino":
                            quantidade_caprinos = quantidade_caprinos + 1
                        elif tipo_atual == "ovino":
                            quantidade_ovinos = quantidade_ovinos + 1
                        elif tipo_atual == "suíno" or tipo_atual == "suino":
                            quantidade_suinos = quantidade_suinos + 1

                        if status_atual == "venda" or status_atual == "engorda" or status_atual == "disponível para venda" or status_atual == "disponivel para venda":
                            animais_disponiveis = animais_disponiveis + 1

                        indice_animal = indice_animal + 1
                    print("\n------ RELATÓRIO ------")
                    print("Bovinos:", quantidade_bovinos)
                    print("Caprinos:", quantidade_caprinos)
                    print("Ovinos:", quantidade_ovinos)
                    print("Suínos:", quantidade_suinos)
                    print("Total de animais:", len(rebanho))
                    print("Animais disponíveis para venda:", animais_disponiveis)

                elif escolha_administrador == "6 - Produção":
                    print("\n--- ATUALIZAR PRODUÇÃO ---")
                    print("Produtos em estoque atualmente:")
                    
                    indice_estoque = 0
                    opcoes_produtos = []
                    while indice_estoque < len(estoque):
                        nome_produto = estoque[indice_estoque]["nome"]
                        quantidade_produto = estoque[indice_estoque]["quantidade"]
                        print("-", nome_produto, "(Quantidade atual:", quantidade_produto, ")")
                        opcoes_produtos.append(nome_produto)
                        indice_estoque = indice_estoque + 1
                    
                    print("-----------------------------------")
                    
                    produto_selecionado = inquirer.select(
                        message="Selecione o produto que deseja abastecer:",
                        choices=opcoes_produtos
                    ).execute()
                    
                    indice_estoque = 0
                    while indice_estoque < len(estoque):
                        if estoque[indice_estoque]["nome"].lower() == produto_selecionado.lower():
                            quantidade_adicionar = float(input("Quantidade para adicionar: "))
                            estoque[indice_estoque]["quantidade"] = estoque[indice_estoque]["quantidade"] + quantidade_adicionar
                            print("Estoque atualizado com sucesso!")
                            break
                        indice_estoque = indice_estoque + 1

                elif escolha_administrador == "7 - Consultar Vendas":
                    print("\n------ HISTÓRICO GLOBAL DE VENDAS ------")
                    if len(historico_compras) == 0:
                        print("Nenhuma venda foi realizada até o momento.")
                    else:
                        indice_venda = 0
                        while indice_venda < len(historico_compras):
                            venda_atual = historico_compras[indice_venda]
                            print("Cliente:", venda_atual["usuario"], "| Produto:", venda_atual["produto"], "| Quantidade:", venda_atual["quantidade"], "| Total: R$", round(venda_atual["valor"], 2), "| Retirada:", venda_atual["retirada"])
                            indice_venda = indice_venda + 1

                elif escolha_administrador == "8 - Sair":
                    print("Saindo do painel ADM...")
                    tipo_logado = ""
                    break

            while tipo_logado == "CLIENTE":
                print("\n--------- MENU CLIENTE ---------")
                
                escolha_cliente = inquirer.select(
                    message="Escolha uma opção:",
                    choices=[
                        "1. Ver estoque e comprar",
                        "2. Histórico de compras",
                        "3. Agendar retirada",
                        "4. Sair"
                    ]
                ).execute()

                if escolha_cliente == "1. Ver estoque e comprar":
                    print("\n                       ------ ESTOQUE ------")
                    opcoes_estoque = []
                    indice_estoque = 0
                    while indice_estoque < len(estoque):
                        sufixo_medida = "Quilos"
                        if estoque[indice_estoque]["nome"] == "Leite":
                            sufixo_medida = "Litros"
                        
                        nome_produto_estoque = estoque[indice_estoque]["nome"]
                        quantidade_produto_estoque = estoque[indice_estoque]["quantidade"]
                        preco_produto_estoque = round(estoque[indice_estoque]["preco"], 2)
                        
                        texto_opcao = f"{nome_produto_estoque} | Quantidade: {quantidade_produto_estoque} {sufixo_medida} | Preço: R$ {preco_produto_estoque}"
                        opcoes_estoque.append({"name": texto_opcao, "value": indice_estoque})
                        indice_estoque = indice_estoque + 1
                        
                    produto_escolhido = inquirer.select(
                        message="Selecione o produto que deseja comprar:",
                        choices=opcoes_estoque
                    ).execute()

                    nome_produto = estoque[produto_escolhido]["nome"]
                    quantidade_estoque = estoque[produto_escolhido]["quantidade"]
                    preco_produto = estoque[produto_escolhido]["preco"]
                    
                    quantidade_desejada = float(input("Digite a quantidade desejada: "))

                    if quantidade_desejada <= quantidade_estoque:
                        valor_total = quantidade_desejada * preco_produto
                        print("Valor total: R$", round(valor_total, 2))
                        
                        confirmar_compra = inquirer.select(
                            message="Confirmar compra?",
                            choices=["Sim", "Não"]
                        ).execute()
                        
                        if confirmar_compra == "Sim":
                            estoque[produto_escolhido]["quantidade"] = estoque[produto_escolhido]["quantidade"] - quantidade_desejada
                            dados_compra = {
                                "usuario": usuario_logado,
                                "produto": nome_produto,
                                "quantidade": quantidade_desejada,
                                "valor": valor_total,
                                "retirada": "Pendente"
                            }
                            historico_compras.append(dados_compra)
                            print("Compra realizada com sucesso!")
                    else:
                        print("Quantidade insuficiente!")

                elif escolha_cliente == "2. Histórico de compras":
                    print("\n------ HISTÓRICO DE COMPRAS ------")
                    total_gasto = 0
                    tem_compra = False

                    indice_compras = 0
                    while indice_compras < len(historico_compras):
                        if historico_compras[indice_compras]["usuario"] == usuario_logado:
                            produto_nome = historico_compras[indice_compras]["produto"]
                            produto_quantidade = historico_compras[indice_compras]["quantidade"]
                            produto_valor = round(historico_compras[indice_compras]["valor"], 2)
                            produto_retirada = historico_compras[indice_compras]["retirada"]

                            print(produto_nome, "| quantidade:", produto_quantidade, "| Total: R$", produto_valor, "| Retirada:", produto_retirada)
                            total_gasto = total_gasto + historico_compras[indice_compras]["valor"]
                            tem_compra = True
                        indice_compras = indice_compras + 1
                        
                    if tem_compra == False:
                        print("Nenhuma compra encontrada!")
                    else:
                        print("\nTotal gasto por você: R$", round(total_gasto, 2))
                        
                        quantidade_queijo = 0
                        quantidade_leite = 0
                        quantidade_carne_bovina = 0
                        quantidade_carne_suina = 0
                        quantidade_carne_caprina = 0
                        
                        indice_compras = 0
                        while indice_compras < len(historico_compras):
                            if historico_compras[indice_compras]["usuario"] == usuario_logado:
                                produto_atual_historico = historico_compras[indice_compras]["produto"]
                                quantidade_atual_historico = historico_compras[indice_compras]["quantidade"]
                                
                                if produto_atual_historico == "Queijo Coalho":
                                    quantidade_queijo = quantidade_queijo + quantidade_atual_historico
                                elif produto_atual_historico == "Leite":
                                    quantidade_leite = quantidade_leite + quantidade_atual_historico
                                elif produto_atual_historico == "Carne Bovina":
                                    quantidade_carne_bovina = quantidade_carne_bovina + quantidade_atual_historico
                                elif produto_atual_historico == "Carne Suína":
                                    quantidade_carne_suina = quantidade_carne_suina + quantidade_atual_historico
                                elif produto_atual_historico == "Carne Caprina":
                                    quantidade_carne_caprina = quantidade_carne_caprina + quantidade_atual_historico
                            indice_compras = indice_compras + 1
                            
                        vendas_totais_cliente = {
                            "Queijo Coalho": quantidade_queijo, 
                            "Leite": quantidade_leite, 
                            "Carne Bovina": quantidade_carne_bovina, 
                            "Carne Suína": quantidade_carne_suina, 
                            "Carne Caprina": quantidade_carne_caprina
                        }
                        
                        produto_mais_comprado = ""
                        maior_quantidade = 0
                        
                        for produto_chave in vendas_totais_cliente:
                            if vendas_totais_cliente[produto_chave] > maior_quantidade:
                                maior_quantidade = vendas_totais_cliente[produto_chave]
                                produto_mais_comprado = produto_chave
                                
                        if maior_quantidade > 0:
                            print("Produto mais comprado por você:", produto_mais_comprado)

                elif escolha_cliente == "3. Agendar retirada":
                    data_retirada = input("Digite a data para retirada nesse formato (dd/mm/yyyy): ")
                    hora_retirada = input("Digite a hora para retirada nesse formato (hh:mm): ")
                    agendamento_realizado = False

                    print("\n==========================================")
                    print("         FAZENDA SERTÃO - RECIBO          ")
                    print("Cliente:", usuario_logado)
                    print("Agendado para:", data_retirada, "as", hora_retirada)
                    print("------------------------------------------")
                
                    indice_compras = 0
                    total_recibo = 0
                    while indice_compras < len(historico_compras):
                        if historico_compras[indice_compras]["usuario"] == usuario_logado and historico_compras[indice_compras]["retirada"] == "Pendente":
                            historico_compras[indice_compras]["retirada"] = data_retirada + " as " + hora_retirada

                            produto_recibo = historico_compras[indice_compras]["produto"]
                            quantidade_recibo = historico_compras[indice_compras]["quantidade"]
                            valor_recibo = round(historico_compras[indice_compras]["valor"], 2)
                            
                            print("-", produto_recibo, "quantidade", quantidade_recibo, "| R$", valor_recibo)
                            total_recibo = total_recibo + historico_compras[indice_compras]["valor"]
                            agendamento_realizado = True
                        indice_compras = indice_compras + 1
                        
                    print("------------------------------------------")
                    print("TOTAL DO PEDIDO: R$", round(total_recibo, 2))
                    print("==========================================")
                    
                    if agendamento_realizado:
                        print("Retirada agendada e recibo emitido com sucesso!")
                    else:
                        print("Você não possui compras pendentes para agendar.")

                elif escolha_cliente == "4. Sair":
                    print("Saindo do painel cliente...")
                    tipo_logado = ""
                    break

    elif opcao_menu_principal == "2. Cadastrar Novo Usuário":
        print("\n------ NOVO USUÁRIO ------")
        novo_usuario = input("Digite o nome do usuário: ")
        nova_senha = input("Digite a senha: ")
        
        tipo_usuario = inquirer.select(
            message="Selecione o perfil do novo usuário:",
            choices=["ADM", "CLIENTE"]
        ).execute()

        usuarios.append({"usuario": novo_usuario, "senha": nova_senha, "perfil": tipo_usuario})
        print("Usuário cadastrado com sucesso!")