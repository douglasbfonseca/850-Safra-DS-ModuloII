import json

with open("Notebooks/cadastro_usuarios.json", "r") as arquivo:
    cadastro = json.loads(arquivo)
    print(cadastro)