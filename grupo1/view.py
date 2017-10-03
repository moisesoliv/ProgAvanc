

class View():
	def __init__(self):
		pass
		
	def mensagemcartao(self, bool cartao):
		if cartao == 1:
			print("Cartão Inserido")
		else:
			print("Insira o cartão")

	def campodesenha(self):
		self.a = str(raw_input("Insira sua senha: "))

	def mensagemsenha(self, senha):
		if self.a != senha:
			print("Senha Incorreta")

	def botaoSaldo(self):
		return True
			
