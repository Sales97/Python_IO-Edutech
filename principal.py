arquivo_contatos = open("dados/contatos.csv", encoding="latin1")

conteudo = arquivo_contatos.readlines()

for linha in conteudo:
    print(linha, end="")