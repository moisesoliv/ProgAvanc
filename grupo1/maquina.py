from Login import *
from View import *
global senha
class Maquina:
    def __init__(self, saldomaq):
        self.saldomaquina = saldomaq
        v = View()
    def monitoracartao(self, cardid):
        self.cardIdentifier = cardid
        if self.cardIdentifier == None:
            print("insira cartao")
        else:
            print("cartao inserido")
            pass

    def mensagem(self):
        pass

    def inputSenhaUser(self,senha):
        v.campoDeSenha()
        self.senha = senha

    def login(self):
        self.loguser = Login(senha)

    def lancaMenuDeOpçoes(self):
        b = v.botaoSaldo()
        s = v.botaoSaque()
        c = v.botaoCancel()
        if b == True:
            self.opcaoSaldo()
        if s == True:
            self.opcaoSaque()
        if c == True:
            self.opcaoCancela()

    def opcaoSaldo(self):







