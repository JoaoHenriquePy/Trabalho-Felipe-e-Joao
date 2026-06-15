from InquirerPy import inquirer

usuarios = [
    {"usuario": "rene", "senha": "123", "perfil": "ADM"},
    {"usuario": "cliente", "senha": "123", "perfil": "CLIENTE"}
]


def login():
    usuario_digitado = input("Usuário: ")
    senha_digitada = input("Senha: ")

    for usuario in usuarios:
        if usuario["usuario"] == usuario_digitado and usuario["senha"] == senha_digitada:
            return usuario

    return None


def cadastrar_usuario():
    print("\n------ CADASTRO DE USUÁRIO ------")

    novo_usuario = input("Nome do usuário: ")
    nova_senha = input("Senha: ")

    perfil = inquirer.select(
        message="Selecione o perfil:",
        choices=["ADM", "CLIENTE"]
    ).execute()

    usuarios.append({
        "usuario": novo_usuario,
        "senha": nova_senha,
        "perfil": perfil
    })

    print("Usuário cadastrado com sucesso!")