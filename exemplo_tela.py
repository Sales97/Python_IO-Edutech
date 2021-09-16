import PySimpleGUI as sg

class Tela_Python:
    def __init__(self):
        #Layout
        layout = [
            [sg.Text("Nome:", size=(5,0)), sg.Input(size=(15,0), key="nome")],
            [sg.Text("Idade:", size=(5,0)), sg.Input(size=(15,0), key="idade")],
            [sg.Text("Quais provedores de email são aceitos?")],
            [sg.Checkbox("gmail", key="gmail"), sg.Checkbox("Outlook", key="outlook"), sg.Checkbox("Yahoo", key="yahoo")],
            [sg.Text("Aceita cartão?")],
            [sg.Radio("sim", "Cartões", key="aceita_cartao"), sg.Radio("Não", "Cartões", key="nao_aceita_cartao")],
            [sg.Button("Enviar Dados")]
        ]

        #Janela
        janela = sg.Window("Dados do Usuário").layout(layout)

        #Extrair Dados da Tela
        self.button, self.values = janela.Read()

    def Iniciar(self):
        nome = self.values["nome"]
        idade = self.values["idade"]
        aceita_gmail = self.values["gmail"]
        aceita_outlook = self.values["outlook"]
        aceita_yahoo = self.values["yahoo"]
        aceita_cartao = self.values["aceita_cartao"]
        nao_aceita_cartao = self.values["nao_aceita_cartao"]

        print(f"nome: {nome}")
        print(f"idade: {idade}")
        print(f"aceita gmail: {aceita_gmail}")
        print(f"aceita outlook: {aceita_outlook}")
        print(f"aceita yahoo: {aceita_yahoo}")
        print(f"aceita cartão: {aceita_cartao}")
        print(f"não aceita cartão: {nao_aceita_cartao}")

tela = Tela_Python()
tela.Iniciar()