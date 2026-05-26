
op = 999

usuarios = [["rene", "123", "ADM"], ["cliente", "456", "CLIENTE"]]
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
    from InquirerPy import prompt
    
    op = [
        {
          "type": "list",

        "message": "Escolha o que você deseja:"
        
        Python?",

        "choices": ["Fazer Login", "Cadastrar Novo Usuário", "Sair do Sistema"]       
        },
    ]
            
    print("\n------- MENU PRINCIPAL -------")
    resuldado = prompt(op)

    if op == 1:
        usuario_digitado = input("Digite seu nome de usuário: ")
        senha_digitada = input("Digite sua senha: ")
        login_ok = False

        i = 0
        while i < len(usuarios):
            nome_usuario = usuarios[i][0]
            senha_usuario = usuarios[i][1]
            tipo_usuario = usuarios[i][2]

            if nome_usuario == usuario_digitado:
                if senha_usuario == senha_digitada:
                    usuario_logado = nome_usuario
                    tipo_logado = tipo_usuario
                    login_ok = True
                    print(f"\nBem-vindo, {usuario_logado}! Perfil: {tipo_logado}")

            i = i + 1
        if login_ok == False:
            print("\nSenha ou nome inválido!")
        else:
            while tipo_logado == "ADM":
                print("\n--------- PAINEL DO ADMINISTRADOR ---------")
                print("1 - Cadastrar Animal")
                print("2 - Buscar Animal")
                print("3 - Atualizar Animal")
                print("4 - Remover Animal")
                print("5 - Relatório")
                print("6 - Produção")
                print("7 - Sair")
                print("-------------------------------------------")
                escolha_adm = input("Escolha: ").lower()

                if escolha_adm == "1" or escolha_adm == "cadastrar":
                    print("\nTipos permitidos: Bovino, Caprino, Ovino, Suino")
                    tipo_animal = input("Digite o tipo do animal: ").lower()

                    while tipo_animal != "bovino" and tipo_animal != "caprino" and tipo_animal != "ovino" and tipo_animal != "suino":
                        print("Tipo inválido!")
                        tipo_animal = input("Digite novamente: ").lower()

                    identificacao_animal = input("Digite a identificação: ")
                    status_animal = input("Digite o status do animal: ")
                    dados_animal = [tipo_animal, identificacao_animal, status_animal]
                    rebanho.append(dados_animal)
                    print("Animal cadastrado com sucesso!")

                elif escolha_adm == "2" or escolha_adm == "buscar":
                    busca = input("Digite a identificação do animal: ").lower()
                    encontrado = False

                    i = 0
                    while i < len(rebanho):
                        id_atual = rebanho[i][1].lower()

                        if id_atual == busca:
                            print("\nAnimal encontrado!")
                            print("Tipo:", rebanho[i][0])
                            print("Identificação:", rebanho[i][1])
                            print("Status:", rebanho[i][2])
                            encontrado = True

                        i = i + 1
                    if encontrado == False:
                        print("Animal não encontrado!")

                elif escolha_adm == "3" or escolha_adm == "atualizar":
                    busca = input("Digite a identificação do animal: ").lower()
                    atualizado = False

                    i = 0
                    while i < len(rebanho):
                        id_atual = rebanho[i][1].lower()

                        if id_atual == busca:
                            print("Animal encontrado!")
                            print("Status atual:", rebanho[i][2])
                            novo_status = input("Digite o novo status: ")
                            rebanho[i][2] = novo_status
                            atualizado = True
                            print("Status atualizado!")

                        i = i + 1
                    if atualizado == False:
                        print("Animal não encontrado!")

                elif escolha_adm == "4" or escolha_adm == "remover":
                    remover = input("Digite a identificação do animal: ").lower()
                    removido = False

                    i = 0
                    while i < len(rebanho):
                        id_atual = rebanho[i][1].lower()

                        if id_atual == remover:
                            del rebanho[i]
                            removido = True
                            print("Animal removido!")
                            break

                        i = i + 1
                    if removido == False:
                        print("Animal não encontrado!")

                elif escolha_adm == "5" or escolha_adm == "relatorio":
                    bovino = 0
                    caprino = 0
                    ovino = 0
                    suino = 0
                    disponivel_venda = 0

                    i = 0
                    while i < len(rebanho):
                        tipo_atual = rebanho[i][0].lower()
                        status_atual = rebanho[i][2].lower()

                        if tipo_atual == "bovino":
                            bovino = bovino + 1

                        elif tipo_atual == "caprino":
                            caprino = caprino + 1

                        elif tipo_atual == "ovino":
                            ovino = ovino + 1

                        elif tipo_atual == "suino":
                            suino = suino + 1

                        if status_atual == "venda" or status_atual == "engorda" or status_atual == "disponivel para venda":
                            disponivel_venda = disponivel_venda + 1

                        i = i + 1
                    print("\n------ RELATÓRIO ------")
                    print("Bovinos:", bovino)
                    print("Caprinos:", caprino)
                    print("Ovinos:", ovino)
                    print("Suinos:", suino)
                    print("Total de animais:", len(rebanho))
                    print("Animais disponíveis para venda:", disponivel_venda)

                elif escolha_adm == "6" or escolha_adm == "producao":
                    print("\n--- ATUALIZAR PRODUÇÃO ---")
                    nome_produto = input("Digite o nome do produto: ")
                    produto_encontrado = False

                    i = 0
                    while i < len(estoque):
                        nome_atual = estoque[i][0].lower()

                        if nome_atual == nome_produto.lower():
                            quantidade_add = float(input("Quantidade para adicionar: "))
                            estoque[i][1] = estoque[i][1] + quantidade_add
                            produto_encontrado = True
                            print("Estoque atualizado!")

                        i = i + 1
                    if produto_encontrado == False:
                        print("Produto não encontrado!")

                elif escolha_adm == "7" or escolha_adm == "sair":
                    print("Saindo do painel ADM...")
                    break

            while tipo_logado == "CLIENTE":
                print("\n--------- MENU CLIENTE ---------")
                print("1. Ver estoque e comprar")
                print("2. Histórico de compras")
                print("3. Agendar retirada")
                print("4. Sair")
                print("--------------------------------")
                escolha_cliente = input("Escolha uma opção: ")

                if escolha_cliente == "1":
                    print("\n------ ESTOQUE ------")

                    i = 0
                    while i < len(estoque):
                        nome_produto = estoque[i][0]
                        quantidade_produto = estoque[i][1]
                        preco_produto = estoque[i][2]
                        print(f"{i+1} - {nome_produto} | Quantidade: {quantidade_produto} | Preço: R${preco_produto:.2f}")

                        i = i + 1
                    produto_escolhido = int(input("\nDigite o número do produto: ")) - 1

                    if produto_escolhido >= 0 and produto_escolhido < len(estoque):
                        nome_produto = estoque[produto_escolhido][0]
                        quantidade_estoque = estoque[produto_escolhido][1]
                        preco_produto = estoque[produto_escolhido][2]
                        quantidade_desejada = float(input("Digite a quantidade desejada: "))

                        if quantidade_desejada <= quantidade_estoque:
                            valor_total = quantidade_desejada * preco_produto
                            print(f"Valor total: R$ {valor_total:.2f}")
                            confirmar = input("Confirmar compra? (s/n)").lower()
                            if confirmar == "s" or confirmar == "sim":
                                estoque[produto_escolhido][1] = estoque[produto_escolhido][1] - quantidade_desejada
                                dados_compra = [
                                    usuario_logado,
                                    nome_produto,
                                    quantidade_desejada,
                                    valor_total,
                                    "Pendente"
                                ]
                                historico_compras.append(dados_compra)
                                print("Compra realizada!")

                        else:
                            print("Quantidade insuficiente!")
                    else:
                        print("Produto inválido!")
                elif escolha_cliente == "2":
                    print("\n------ HISTÓRICO ------")
                    total_gasto = 0
                    tem_compra = False
                    contagem = [
                        ["Queijo Coalho", 0],
                        ["Queijo Manteiga", 0],
                        ["Leitão", 0],
                        ["Leite (Litros)", 0]
                    ]

                    i = 0
                    while i < len(historico_compras):
                        usuario_compra = historico_compras[i][0]

                        if usuario_compra == usuario_logado:
                            nome_produto = historico_compras[i][1]
                            quantidade = historico_compras[i][2]
                            valor = historico_compras[i][3]
                            retirada = historico_compras[i][4]
                            print(f"{nome_produto} | Qtd: {quantidade} | Total: R${valor:.2f} | Retirada: {retirada}")
                            total_gasto = total_gasto + valor
                            tem_compra = True

                            c = 0
                            while c < len(contagem):
                                if contagem[c][0] == nome_produto:
                                    contagem[c][1] = contagem[c][1] + 1
                                c = c + 1

                        i = i + 1
                    if tem_compra == False:
                        print("Nenhuma compra encontrada!")
                    else:
                        print(f"\nTotal gasto: R$ {total_gasto:.2f}")
                        maior = 0
                        produto_mais = ""

                        i = 0
                        while i < len(contagem):

                            if contagem[i][1] > maior:
                                maior = contagem[i][1]
                                produto_mais = contagem[i][0]

                            i = i + 1
                        if produto_mais != "":
                            print("Produto mais comprado:", produto_mais)

                elif escolha_cliente == "3":
                    data = input("Digite a data: ")
                    hora = input("Digite a hora: ")

                    i = 0
                    while i < len(historico_compras):
                        if historico_compras[i][0] == usuario_logado:
                            if historico_compras[i][4] == "Pendente":
                                historico_compras[i][4] = data + " às " + hora
                        i = i + 1
                    print("Retirada agendada!")

                elif escolha_cliente == "4":
                    print("Saindo do painel cliente...")

                    break

    elif op == 2:
        print("\n------ NOVO USUÁRIO ------")
        novo_usuario = input("Digite o nome do usuário: ")
        nova_senha = input("Digite a senha: ")
        tipo_usuario = input("Digite ADM ou CLIENTE: ").upper()

        while tipo_usuario != "ADM" and tipo_usuario != "CLIENTE":
            print("Tipo inválido!")
            tipo_usuario = input("Digite ADM ou CLIENTE: ").upper()
        novo_cadastro = [novo_usuario, nova_senha, tipo_usuario]
        usuarios.append(novo_cadastro)
        print("Usuário cadastrado com sucesso!")
    elif op == 3:
        print("\nSistema encerrado com sucesso.")