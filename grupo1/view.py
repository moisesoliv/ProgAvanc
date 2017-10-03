

class View():
	def __init__(self, saque):
		self.saque = saque

	def mensagem(self):
		print("Cartão Inserido")

	def campodesenha(self):
		a = str(raw_input("Insira sua senha: "))
		
