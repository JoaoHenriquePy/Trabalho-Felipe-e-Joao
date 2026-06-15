from datetime import datetime
from rich.console import Console
from rich.table import Table
import requests

console = Console()

rebanho = []

estoque = [
    {"nome": "Queijo Coalho", "quantidade": 120.0, "preco": 42.90},
    {"nome": "Leite", "quantidade": 50.0, "preco": 3.50},
    {"nome": "Carne Bovina", "quantidade": 200.0, "preco": 25.00},
    {"nome": "Carne Suína", "quantidade": 150.0, "preco": 20.00},
    {"nome": "Carne Caprina", "quantidade": 100.0, "preco": 30.00}
]

historico_compras = []
historico_movimentacao = []
producao_leite = []
vacinas = []
lista_desejos = []


def registrar_movimentacao(acao, item, qtd):
    historico_movimentacao.append(
        {
            "data": datetime.now().strftime("%d/%m/%Y"),
            "acao": acao,
            "item": item,
            "qtd": qtd
        }
    )


def cadastrar_animal():
    tipo = input(
        "Tipo (Bovino de Leite, Caprino, Ovino, Suíno/Leitão): "
    )

    identificacao = input(
        "Identificação (brinco/número): "
    )

    status = input(
        "Status do animal: "
    )

    peso = float(
        input("Peso (kg): ")
    )

    rebanho.append(
        {
            "tipo": tipo,
            "identificacao": identificacao,
            "status": status,
            "peso": peso
        }
    )

    print("Animal cadastrado com sucesso!")


def buscar_animal():
    busca = input("Identificação: ").lower()

    for animal in rebanho:
        if animal["identificacao"].lower() == busca:
            print(animal)
            return

    print("Animal não encontrado.")


def atualizar_animal():
    busca = input("Identificação: ").lower()

    for animal in rebanho:
        if animal["identificacao"].lower() == busca:
            novo_status = input("Novo status: ")
            animal["status"] = novo_status
            print("Atualizado!")
            return

    print("Animal não encontrado.")


def remover_animal():
    busca = input("Identificação: ").lower()

    for animal in rebanho:
        if animal["identificacao"].lower() == busca:
            rebanho.remove(animal)
            print("Animal removido!")
            return

    print("Animal não encontrado.")


def registrar_producao_leite():
    litros = float(
        input("Litros produzidos hoje: ")
    )

    producao_leite.append(
        {
            "data": datetime.now().strftime("%d/%m/%Y"),
            "litros": litros
        }
    )

    registrar_movimentacao(
        "produção",
        "Leite",
        litros
    )

    print("Produção registrada!")


def adicionar_produto():
    nome = input("Produto: ")

    quantidade = float(
        input("Quantidade kg/litros: ")
    )

    preco = float(
        input("Preço de venda: ")
    )

    estoque.append(
        {
            "nome": nome,
            "quantidade": quantidade,
            "preco": preco
        }
    )

    registrar_movimentacao(
        "produção",
        nome,
        quantidade
    )

    print("Produto cadastrado!")


def registrar_vacina():
    animal = input("Identificação do animal: ")
    vacina = input("Nome da vacina: ")

    vacinas.append(
        {
            "animal": animal,
            "vacina": vacina,
            "data": datetime.now().strftime("%d/%m/%Y")
        }
    )

    print("Vacinação registrada!")


def dashboard():
    tabela = Table(title="RELATÓRIO GERAL")

    tabela.add_column("Item")
    tabela.add_column("Quantidade")

    bovinos = 0
    caprinos = 0
    ovinos = 0
    suinos = 0

    for animal in rebanho:

        tipo = animal["tipo"].lower()

        if "bovino" in tipo:
            bovinos += 1

        elif "caprino" in tipo:
            caprinos += 1

        elif "ovino" in tipo:
            ovinos += 1

        elif "su" in tipo:
            suinos += 1

    tabela.add_row("Bovinos", str(bovinos))
    tabela.add_row("Caprinos", str(caprinos))
    tabela.add_row("Ovinos", str(ovinos))
    tabela.add_row("Suínos", str(suinos))

    total_leite = 0

    for prod in producao_leite:
        total_leite += prod["litros"]

    tabela.add_row(
        "Litros Produzidos",
        str(total_leite)
    )

    console.print(tabela)

    estoque_table = Table(title="ESTOQUE")

    estoque_table.add_column("Produto")
    estoque_table.add_column("Quantidade")
    estoque_table.add_column("Preço")

    for item in estoque:
        estoque_table.add_row(
            item["nome"],
            str(item["quantidade"]),
            f'R$ {item["preco"]}'
        )

    console.print(estoque_table)


def consultar_movimentacoes():
    for mov in historico_movimentacao:
        print(
            mov["data"],
            mov["acao"],
            mov["item"],
            mov["qtd"]
        )


def consultar_clima():
    try:
        resposta = requests.get(
            "https://wttr.in/Sousa?format=3"
        )

        print(resposta.text)

    except:
        print("Erro ao consultar clima.")


def adicionar_desejo(usuario):
    produto = input("Produto desejado: ")

    lista_desejos.append(
        {
            "usuario": usuario,
            "produto": produto
        }
    )

    print("Desejo registrado!")