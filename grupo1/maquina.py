from Login import *
from View import *
class Maquina:
    def __init__(self, saldomaq):
        self.saldomaquina = saldomaq
        self.v = View()
        self.cartao = Cartao()

    def monitoracartao(self):
        self.cardId = self.cartao.cardIdentifier
        if self.cardId == None:
            self.v.mensagemCartao(True)
        else:
            self.v.mensagemCartao(False)
            pass

    def inputSenhaUser(self):
        self.senha = self.v.campoDeSenha()

    def login(self):
        self.loguser = Login(senha)
        self.loguser.verificaSenha()
        self.loguser.atualizaChances()
        self.loguser.validaCartao()

    def lancaMenuDeOpçoes(self):
        b = self.v.botaoSaldo()
        s = self.v.botaoSaque()
        c = self.v.botaoCancel()
        if b == True:
            self.opcaoSaldo()
        if s == True:
            self.opcaoSaque()
        if c == True:
            self.opcaoCancela()

    def opcaoSaldo(self):
        self.saldocartao = self.cartao.enviaSaldo()
        self.v.campoDeSaldo(self.saldocartao)

    def opcaoSaque(self):
        self.saldocartao = self.cartao.enviaSaldo()
        self.valorSaque = self.v.campoDeSaque()
        if self.saldocartao >= self.valorSaque:
            if self.saldomaquina >= self.valorSaque:
                self.ejetaValor()


    def ejetaValor(self):
        self.saldomaquina -= self.valorSaque
        self.saldocartao -= self.valorSaque
        self.cartao.atualizaSaldo(self.saldocartao)

    def opcaoCancela(self):
        self.monitoracartao()



def main:
    m = Maquina(100000000.00)
    m.monitoracartao()




if __name__=="__main__":
    main()



