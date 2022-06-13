from encodings import utf_8
import json

def cadastrar(cadastro):
    nome = input("Digite o nome:")
    cpf = input("Digite o CPF:")
    email = input("Digite o email:")


def cadastrar_novos_usuarios():
    with open("cadastro_usuario.json", "w", encoding="utf8") as arquivo:
        cadastro = json.loads(arquivo)
        print("Cadastre o novo usuário, as informações obrigatórias são: Nome, CPF e e-mail, as opcionais são: data de nascimento, profissão e escolaridade.")
        cadastrar(cadastro)
def buscar_usuarios():
def modificar_usuarios():
def visualizar_all_usuarios():

def menu():
    lista_opc_validas = list("01234")
    opc0 = "0-Sair"
    opc1 = "1-Cadastrar novos usuários"
    opc2 = "2-Buscar usuários já existentes"
    opc3 = "3-Modificar um usuário já existente"
    opc4 = "4-visualizar todos os usuários"
    opc_usuario = ""

    dict_opc = {
        "1" : cadastrar_novos_usuarios(),
        "2" : buscar_usuarios(),
        "3" : modificar_usuarios(),
        "4" : visualizar_all_usuarios()
        }
      
    while opc_usuario != "0":
        opc_usuario = input(f"Escolha uma opção:\n{opc0}\n{opc1}\n{opc2}\n{opc3}\n{opc4}\n")
        if opc_usuario not in lista_opc_validas:
            print("opcao inválida!")
            continue
        dict_opc[opc_usuario]

menu()