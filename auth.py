from InquirerPy import inquirer
from validator_collection import validators

usuarios = [
    {"usuario": "rene", "senha": "123", "perfil": "ADM"},
    {"usuario": "cliente", "senha": "123", "perfil": "CLIENTE"}
]


def login():
    usuario_digitado = input("Usuário: ").strip()
    senha_digitada = input("Senha: ").strip()

    for usuario in usuarios:
        if usuario["usuario"] == usuario_digitado and usuario["senha"] == senha_digitada:
            return usuario
    return None


def cadastrar_usuario():
    print("\n------ CADASTRO DE USUÁRIO ------")

    usuario_input = input("Nome do usuário: ").strip()
    if not usuario_input:
        print("Erro: O nome do usuário não pode ficar em branco!")
        return

    senha_input = input("Senha: ").strip()
    if not senha_input:
        print("Erro: A senha não pode ficar em branco!")
        return

    perfil = inquirer.select(
        message="Selecione o perfil:",
        choices=["ADM", "CLIENTE"]
    ).execute()

    usuarios.append({
        "usuario": usuario_input,
        "senha": senha_input,
        "perfil": perfil
    })
    print("Usuário cadastrado com sucesso!")