class Login:
    def __init__(self,senhaDoCartao):
        self.recebeSenha = senhaDoCartao
        self.chances = 3
    def verificaSenha(self,recebeSenha,senhaDigitada):
        if(self.chances>0):
            if(recebeSenha == senhaDigitada):
                return  True
            else:
                return False
        break

    def atualizaChances(self):
        self.chances = self.chances -1
