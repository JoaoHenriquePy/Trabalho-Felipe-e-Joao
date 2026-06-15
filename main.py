from InquirerPy import inquirer

from auth import (
    login,
    cadastrar_usuario
)

from fazenda import (
    estoque,
    historico_compras,
    cadastrar_animal,
    buscar_animal,
    atualizar_animal,
    remover_animal,
    registrar_producao_leite,
    adicionar_produto,
    registrar_vacina,
    dashboard,
    consultar_movimentacoes,
    consultar_clima,
    adicionar_desejo,
    registrar_movimentacao
)

opcao_principal = ""

while opcao_principal != "3":

    print("\n===== SISTEMA FAZENDA SERTÃO =====")

    opcao_principal = inquirer.select(
        message="Escolha uma opção:",
        choices=[
            {"name": "1 - Fazer Login", "value": "1"},
            {"name": "2 - Cadastrar Usuário", "value": "2"},
            {"name": "3 - Sair", "value": "3"}
        ]
    ).execute()

    if opcao_principal == "1":

        usuario = login()

        if usuario is None:
            print("Usuário ou senha inválidos.")
            continue

        usuario_logado = usuario["usuario"]
        perfil = usuario["perfil"]

        print(
            f"\nBem-vindo {usuario_logado}"
        )

        while perfil == "ADM":

            opcao_adm = inquirer.select(
                message="Painel ADM",
                choices=[
                    "1 - Cadastrar Animal",
                    "2 - Buscar Animal",
                    "3 - Atualizar Animal",
                    "4 - Remover Animal",
                    "5 - Registrar Produção de Leite",
                    "6 - Adicionar Produto ao Estoque",
                    "7 - Dashboard Geral",
                    "8 - Registrar Vacinação",
                    "9 - Histórico de Movimentação",
                    "10 - Consultar Clima",
                    "11 - Consultar Vendas",
                    "12 - Sair"
                ]
            ).execute()

            if opcao_adm == "1 - Cadastrar Animal":
                cadastrar_animal()

            elif opcao_adm == "2 - Buscar Animal":
                buscar_animal()

            elif opcao_adm == "3 - Atualizar Animal":
                atualizar_animal()

            elif opcao_adm == "4 - Remover Animal":
                remover_animal()

            elif opcao_adm == "5 - Registrar Produção de Leite":
                registrar_producao_leite()

            elif opcao_adm == "6 - Adicionar Produto ao Estoque":
                adicionar_produto()

            elif opcao_adm == "7 - Dashboard Geral":
                dashboard()

            elif opcao_adm == "8 - Registrar Vacinação":
                registrar_vacina()

            elif opcao_adm == "9 - Histórico de Movimentação":
                consultar_movimentacoes()

            elif opcao_adm == "10 - Consultar Clima":
                consultar_clima()

            elif opcao_adm == "11 - Consultar Vendas":

                print("\n===== VENDAS =====")

                if len(historico_compras) == 0:
                    print("Nenhuma venda realizada.")
                else:

                    for venda in historico_compras:

                        print(
                            f"Cliente: {venda['usuario']} | "
                            f"Produto: {venda['produto']} | "
                            f"Qtd: {venda['quantidade']} | "
                            f"Valor: R$ {round(venda['valor'],2)} | "
                            f"Retirada: {venda['retirada']}"
                        )

            elif opcao_adm == "12 - Sair":
                break

        while perfil == "CLIENTE":

            opcao_cliente = inquirer.select(
                message="Menu Cliente",
                choices=[
                    "1 - Comprar Produtos",
                    "2 - Histórico de Compras",
                    "3 - Agendar Retirada",
                    "4 - Lista de Desejos",
                    "5 - Consultar Clima",
                    "6 - Sair"
                ]
            ).execute()

            if opcao_cliente == "1 - Comprar Produtos":

                opcoes = []

                for i, item in enumerate(estoque):

                    texto = (
                        f"{item['nome']} | "
                        f"Qtd: {item['quantidade']} | "
                        f"Preço: R$ {item['preco']}"
                    )

                    opcoes.append(
                        {
                            "name": texto,
                            "value": i
                        }
                    )

                produto = inquirer.select(
                    message="Escolha o produto",
                    choices=opcoes
                ).execute()

                qtd = float(
                    input("Quantidade desejada: ")
                )

                if qtd <= estoque[produto]["quantidade"]:

                    total = (
                        qtd *
                        estoque[produto]["preco"]
                    )

                    print(
                        f"Valor total: R$ {round(total,2)}"
                    )

                    confirmar = inquirer.select(
                        message="Confirmar compra?",
                        choices=["Sim", "Não"]
                    ).execute()

                    if confirmar == "Sim":

                        estoque[produto]["quantidade"] -= qtd

                        historico_compras.append(
                            {
                                "usuario": usuario_logado,
                                "produto": estoque[produto]["nome"],
                                "quantidade": qtd,
                                "valor": total,
                                "retirada": "Pendente"
                            }
                        )

                        registrar_movimentacao(
                            "venda",
                            estoque[produto]["nome"],
                            qtd
                        )

                        print(
                            "Compra realizada!"
                        )

                else:
                    print(
                        "Quantidade insuficiente."
                    )

            elif opcao_cliente == "2 - Histórico de Compras":

                encontrou = False
                total_gasto = 0

                for compra in historico_compras:

                    if compra["usuario"] == usuario_logado:

                        encontrou = True

                        print(
                            f"{compra['produto']} | "
                            f"Qtd {compra['quantidade']} | "
                            f"R$ {round(compra['valor'],2)} | "
                            f"{compra['retirada']}"
                        )

                        total_gasto += compra["valor"]

                if encontrou:
                    print(
                        f"\nTotal gasto: R$ {round(total_gasto,2)}"
                    )
                else:
                    print(
                        "Nenhuma compra encontrada."
                    )

            elif opcao_cliente == "3 - Agendar Retirada":

                consultar_clima()

                data = input(
                    "Data (dd/mm/aaaa): "
                )

                hora = input(
                    "Hora (hh:mm): "
                )

                total = 0
                encontrou = False

                print("\n")
                print("=" * 40)
                print("RECIBO DE RETIRADA")
                print("=" * 40)

                print(
                    "Cliente:",
                    usuario_logado
                )

                print(
                    "Agendado para:",
                    data,
                    hora
                )

                print("-" * 40)

                for compra in historico_compras:

                    if (
                        compra["usuario"] == usuario_logado
                        and compra["retirada"] == "Pendente"
                    ):

                        compra["retirada"] = (
                            data +
                            " às " +
                            hora
                        )

                        print(
                            compra["produto"],
                            "| Qtd:",
                            compra["quantidade"],
                            "| R$",
                            round(compra["valor"], 2)
                        )

                        total += compra["valor"]
                        encontrou = True

                print("-" * 40)
                print(
                    "TOTAL:",
                    round(total, 2)
                )
                print("=" * 40)

                if encontrou:
                    print(
                        "Retirada agendada!"
                    )
                else:
                    print(
                        "Nenhuma compra pendente."
                    )

            elif opcao_cliente == "4 - Lista de Desejos":
                adicionar_desejo(
                    usuario_logado
                )

            elif opcao_cliente == "5 - Consultar Clima":
                consultar_clima()

            elif opcao_cliente == "6 - Sair":
                break

    elif opcao_principal == "2":
        cadastrar_usuario()

print("Sistema encerrado.")