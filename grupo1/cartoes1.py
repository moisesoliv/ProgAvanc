class Cartao():
    def __init__(self,b,c,d):
        self.cardIdentifier = b
        self.senhaDoCartao = c
        self.saldoCartao = d

    def senhaCartao(self):
        return self.senhaDoCartao
    def identifier(self):
        return self.cardIdentifier
    def saldo(self):
        return self.saldoCartao

#### main()

#cr = csv.reader(open("MEUARQUIVO.csv","rb"))

#b = input('nome')
b = 'tunaktunaktun'
#c = int(input('senha'))
c = 123123
#d = int(input('saldo'))
d = 900

a = Cartao(b,c,d)
#print(a.senhaCartao())
#print(a.identifier())
#print(a.saldo())