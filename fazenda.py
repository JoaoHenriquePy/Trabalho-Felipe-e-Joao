from datetime import datetime
from rich.console import Console
from rich.table import Table
import requests
import cowsay

console = Console()

# Dados principais
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
    historico_movimentacao.append({
        "data": datetime.now().strftime("%d/%m/%Y"),
        "acao": acao,
        "item": item,
        "qtd": qtd
    })


def cadastrar_animal():
    tipo = input("Tipo (Bovino de Leite, Caprino, Ovino, Suíno/Leitão): ").strip()
    if not tipo:
        print("Erro: O tipo não pode ficar vazio!")
        return

    identificacao = input("Identificação (brinco/número): ").strip()
    if not identificacao:
        print("Erro: A identificação não pode ficar vazia!")
        return

    status = input("Status do animal: ").strip()
    peso = float(input("Peso (kg): "))

    rebanho.append({
        "identificacao": identificacao,
        "tipo": tipo,
        "status": status,
        "peso": peso
    })
    cowsay.cow("Animal cadastrado com sucesso!")


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
            novo_status = input("Novo status: ").strip()
            animal["status"] = novo_status
            print("Animal atualizado com sucesso!")
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
    litros = float(input("Litros produzidos hoje: "))
    producao_leite.append({
        "data": datetime.now().strftime("%d/%m/%Y"),
        "litros": litros
    })

    for item in estoque:
        if item["nome"] == "Leite":
            item["quantidade"] += litros

    registrar_movimentacao("produção", "Leite", litros)
    print("Produção registrada e estoque atualizado!")


def adicionar_produto():
    nome = input("Nome do produto: ").strip()
    if not nome:
        print("Erro: Nome não pode ficar vazio!")
        return

    quantidade = float(input("Quantidade: "))
    preco = float(input("Preço de venda: "))

    estoque.append({"nome": nome, "quantidade": quantidade, "preco": preco})
    registrar_movimentacao("produção", nome, quantidade)
    print("Produto adicionado ao estoque!")


def registrar_vacina():
    animal = input("Identificação do animal: ").strip()
    if not animal:
        print("Erro: Identificação não pode ficar vazia!")
        return
    vacina = input("Nome da vacina: ").strip()
    if not vacina:
        print("Erro: Nome da vacina não pode ficar vazio!")
        return

    vacinas.append({
        "animal": animal,
        "vacina": vacina,
        "data": datetime.now().strftime("%d/%m/%Y")
    })
    print("Vacinação registrada!")


def dashboard():
    tabela = Table(title="RELATÓRIO GERAL DA FAZENDA")
    tabela.add_column("Item")
    tabela.add_column("Quantidade")

    bovinos = sum(1 for a in rebanho if "bovino" in a["tipo"].lower())
    caprinos = sum(1 for a in rebanho if "caprino" in a["tipo"].lower())
    ovinos = sum(1 for a in rebanho if "ovino" in a["tipo"].lower())
    suinos = sum(1 for a in rebanho if "su" in a["tipo"].lower())

    tabela.add_row("Bovinos", str(bovinos))
    tabela.add_row("Caprinos", str(caprinos))
    tabela.add_row("Ovinos", str(ovinos))
    tabela.add_row("Suínos", str(suinos))

    total_leite = sum(p["litros"] for p in producao_leite)
    tabela.add_row("Total de Leite", str(total_leite))

    console.print(tabela)

    # Estoque
    est = Table(title="ESTOQUE ATUAL")
    est.add_column("Produto")
    est.add_column("Quantidade")
    est.add_column("Preço")
    for item in estoque:
        est.add_row(item["nome"], str(item["quantidade"]), f"R$ {item['preco']:.2f}")
    console.print(est)


def consultar_movimentacoes():
    print("\n=== HISTÓRICO DE MOVIMENTAÇÃO ===")
    if not historico_movimentacao:
        print("Ainda não há movimentações.")
        return
    for mov in historico_movimentacao:
        print(f"{mov['data']} | {mov['acao']} | {mov['item']} | {mov['qtd']}")


def consultar_clima():
    resposta = requests.get("https://wttr.in/Sousa?format=3")
    print(resposta.text)


def adicionar_desejo(usuario):
    produto = input("Produto desejado: ").strip()
    if not produto:
        print("Erro: O produto não pode ficar vazio!")
        return
    lista_desejos.append({"usuario": usuario, "produto": produto})
    print("Desejo registrado!")