arquivo_contatos = open('dados/contatos.csv', encoding="latin_1", mode="a+")
#open: abre o arquivo, enconding: , mode: pode ser r(read), w(write), a(write,appending to the end)
#mode = "w+" ou "a+"-> escrita e leitura

for linha in arquivo_contatos:
    print(linha, end="")
#lendo o arquivo!

contato_novo = "11,Carol,carol@carol.com.br\n"
arquivo_contatos.write(contato_novo)
#ou
contatos = ["12,Carol1,carol1@carol1.com.br\n"
            "13,Carol2,carol2@carol2.com.br\n"
            "14,Carol3,carol3@carol3.com.br\n"]
for contato in contatos:
    arquivo_contatos.write(contato)
#escrevendo no arquivo!(é preciso estar no modo de escrita!)

arquivo_contatos.close()
#Indica que o arquivo não será mais trabalhado, encerrando suas tarefas

arquivo_contatos.flush()
#Força o encerramento da escrita do arquivo, mas ainda o deixa aberto

arquivo_contatos.seek(0)
#Faz o arquivo iterar a partir do caractere 0

try:
    arquivo_contatos = open("arquivo_q_n_existe.csv", mode="w+")
    for linha in arquivo_contatos:
        print(linha, end="")
except FileNotFoundError: #Tratando exceções!
    print("Arquivo não encontrado")
except PermissionError:
    print("Sem permissão de escrita")
finally: #independente das exceções (erros), o finally será executado
    arquivo_contatos.close()

with open('dados/contatos.csv') as arquivo_contatos:
    arquivo_contatos.write("variável_exemplo")
#O arquivo é aberto e fechado com o statement
#Recurso usado em contextos específicos

arquivo = open("dados/contatos.csv", encoding="latin_1", mode="a+")
contato = bytes("15,Verônica,veronica@veronica.com.br\n", "latin_1")
arquivo.buffer.write(contato)
#escrevendo diretamente pelo buffer!