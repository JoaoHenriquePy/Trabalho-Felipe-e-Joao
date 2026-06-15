from InquirerPy import inquirer
import cowsay

from auth import login, cadastrar_usuario
from fazenda import (
    estoque, historico_compras, cadastrar_animal, buscar_animal,
    atualizar_animal, remover_animal, registrar_producao_leite,
    adicionar_produto, registrar_vacina, dashboard,
    consultar_movimentacoes, consultar_clima, adicionar_desejo,
    registrar_movimentacao
)
from telas import exibir_menu_principal, exibir_menu_adm, exibir_menu_cliente

opcao_principal = ""

while opcao_principal != "3":
    opcao_principal = exibir_menu_principal()

    if opcao_principal == "1":
        usuario = login()
        if not usuario:
            print("Usuário ou senha inválidos.")
            continue

        usuario_logado = usuario["usuario"]
        perfil = usuario["perfil"]

        cowsay.cow(f"Bem-vindo, {usuario_logado}!")

        while perfil == "ADM":
            opcao = exibir_menu_adm()
            if opcao == "1 - Cadastrar Animal":
                cadastrar_animal()
            elif opcao == "2 - Buscar Animal":
                buscar_animal()
            elif opcao == "3 - Atualizar Animal":
                atualizar_animal()
            elif opcao == "4 - Remover Animal":
                remover_animal()
            elif opcao == "5 - Registrar Produção de Leite":
                registrar_producao_leite()
            elif opcao == "6 - Adicionar Produto ao Estoque":
                adicionar_produto()
            elif opcao == "7 - Dashboard Geral":
                dashboard()
            elif opcao == "8 - Registrar Vacinação":
                registrar_vacina()
            elif opcao == "9 - Histórico de Movimentação":
                consultar_movimentacoes()
            elif opcao == "10 - Consultar Clima":
                consultar_clima()
            elif opcao == "11 - Consultar Vendas":
                print("\n===== VENDAS REALIZADAS =====")
                if not historico_compras:
                    print("Nenhuma venda ainda.")
                else:
                    for v in historico_compras:
                        print(f"Cliente: {v['usuario']} | {v['produto']} | Qtd: {v['quantidade']} | R$ {v['valor']:.2f}")
            elif opcao == "12 - Sair":
                perfil = ""

        while perfil == "CLIENTE":
            opcao = exibir_menu_cliente()
            if opcao == "1 - Comprar Produtos":
                opcoes = []
                for i, item in enumerate(estoque):
                    opcoes.append({
                        "name": f"{item['nome']} (Estoque: {item['quantidade']}) - R${item['preco']}",
                        "value": i
                    })
                
                indice = inquirer.select(message="Escolha o produto", choices=opcoes).execute()

                qtd = float(input("Quantidade desejada: "))
                if qtd > estoque[indice]["quantidade"]:
                    print("Quantidade insuficiente no estoque!")
                else:
                    total = qtd * estoque[indice]["preco"]
                    print(f"Valor total: R$ {total:.2f}")

                    confirmar = inquirer.select(message="Confirmar compra?", choices=["Sim", "Não"]).execute()
                    if confirmar == "Sim":
                        estoque[indice]["quantidade"] -= qtd
                        historico_compras.append({
                            "usuario": usuario_logado,
                            "produto": estoque[indice]["nome"],
                            "quantidade": qtd,
                            "valor": total,
                            "retirada": "Pendente"
                        })
                        registrar_movimentacao("venda", estoque[indice]["nome"], qtd)
                        print("Compra realizada com sucesso!")

            elif opcao == "2 - Histórico de Compras":
                total_gasto = 0
                encontrou = False
                for c in historico_compras:
                    if c["usuario"] == usuario_logado:
                        print(f"{c['produto']} | Qtd: {c['quantidade']} | R$ {c['valor']:.2f} | {c['retirada']}")
                        total_gasto += c["valor"]
                        encontrou = True
                if encontrou:
                    print(f"\nTotal gasto: R$ {total_gasto:.2f}")
                else:
                    print("Você ainda não fez nenhuma compra.")

            elif opcao == "3 - Agendar Retirada":
                pendentes = [c for c in historico_compras if c["usuario"] == usuario_logado and c["retirada"] == "Pendente"]
                if not pendentes:
                    print("Você não tem compras pendentes.")
                else:
                    consultar_clima()
                    data = input("Data da retirada (dd/mm/aaaa): ")
                    hora = input("Hora (hh:mm): ")

                    print("\n" + "="*55)
                    print("       RECIBO DE RETIRADA - FAZENDA SERTÃO")
                    print("="*55)
                    print(f"Cliente : {usuario_logado}")
                    print(f"Data    : {data} às {hora}")
                    print("-"*55)
                    total = 0
                    for compra in pendentes:
                        print(f"{compra['produto']:25} | Qtd: {compra['quantidade']:6} | R$ {compra['valor']:.2f}")
                        total += compra["valor"]
                        compra["retirada"] = f"{data} às {hora}"
                    print("-"*55)
                    print(f"TOTAL   : R$ {total:.2f}")
                    print("="*55)
                    print("Retirada agendada!")

            elif opcao == "4 - Lista de Desejos":
                adicionar_desejo(usuario_logado)
            elif opcao == "5 - Consultar Clima":
                consultar_clima()
            elif opcao == "6 - Sair":
                perfil = ""

print("Sistema encerrado.")