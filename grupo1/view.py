

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

	def campoSaldo(self, saldo):
		self.saldo = saldo
		print("RS %f.2",saldo)

	def campoDeSaque(self):
		self.s = float(raw_input("Digite o valor desejado: "))
		if s > self.saldo:
			print("Saldo Insuficiente")
		

	def botaoSaque(self):
		return True
