class Cartao():
	def __init__(self,cardIdentifier,senhaDoCartao,saldoCartao):
		self.cardIdentifier = cardIdentifier
		self.senhaDoCartao = senhaDoCartao
		self.saldoCartao = float(saldoCartao)/100

cartoes = [] 

def criaObj():
	import csv 
	p = open("cartoes.csv", 'r')
	print p


	for linha in p.readlines():
		elementos = linha.split(',')
		cartoes.append(Cartao(elementos[0],elementos[1],elementos[2]))

criaObj()

def id(identificador):
	for i in cartoes:
		if i.cardIdentifier == identificador:
			return identificador
	return 'Erro'

def senha(identificador):
	for i in cartoes:
		if i.cardIdentifier == identificador:
			return i.senhaDoCartao
	return 'Erro'

def saldo(identificador):
	for i in cartoes:
		if i.cardIdentifier == identificador:
			return i.saldoCartao
	return 'Erro'





