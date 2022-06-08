import csv

#nota_aprovacao = int(input("Digite a nota mínima de aprovação:"))
nota_aprovacao = 7

try:    
    with open("Notebooks/notas_alunos.csv", "r", encoding="utf8") as entrada, open("Notebooks/aprovacao_alunos.csv", "w", encoding="utf8") as saida:
        tabela_notas = list(csv.reader(entrada, delimiter=';', lineterminator='\n'))
        
        for linha in tabela_notas:
            for i in range(1, len(linha)):
                try:
                    linha[i] = float(linha[i])
                except ValueError:
                    linha[i] = 0
                    print(f"A nota {i} do/a aluno/a {linha[0]} não pode ser interpretada como float")
                try:
                    if not 0 <= linha[i] <= 10:
                        linha[i] = 0
                        raise Exception(f"A nota {i} do/a aluno/a {linha[0]} está fora do intervalo válido 0-10")
                except:
                    print(f"A nota {i} do/a aluno/a {linha[0]} está fora do intervalo válido 0-10")
                
            media = sum(linha[1:])/(len(linha)-1)
            linha.append(media)
            linha.append("APR" if media >= nota_aprovacao else "REP")
        
        try:
            escritor = csv.writer(saida, delimiter=";", lineterminator="\n")
            escritor.writerows(tabela_notas)
        except:
            print("Não foi possível criar o arquivo \n",tabela_notas)
except:
    print("Não foi possível abrir o aquivo original.")