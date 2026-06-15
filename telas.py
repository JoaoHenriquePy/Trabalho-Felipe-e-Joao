from InquirerPy import inquirer

def exibir_menu_principal():
    print("\n===== SISTEMA FAZENDA SERTÃO =====")
    return inquirer.select(
        message="Escolha uma opção:",
        choices=[
            {"name": "1 - Fazer Login", "value": "1"},
            {"name": "2 - Cadastrar Usuário", "value": "2"},
            {"name": "3 - Sair", "value": "3"}
        ]
    ).execute()


def exibir_menu_adm():
    return inquirer.select(
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


def exibir_menu_cliente():
    return inquirer.select(
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