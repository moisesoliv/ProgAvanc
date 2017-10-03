View():
	def __init__(self,valorDeSaque):
		self.valorDeSaque = float(valorDeSaque)

	def menu(self):
		print("Pressione s para efetuar saque, a para consultar saldo ou c para cancelar a operacao")
		resposta = input()
		return resposta

	def mensagemcartao(self, bool(cartao)):
		if cartao == 1:
			print("Cartao inserido")
		else:
			print("Insira o cartao")


	def mensagemSenha(self, senha)
		if self.campo == senha:
			print("Senha correta")

		else:
			print("Senha incorreta")

	def campoDesenha(self):
		print("Digite sua senha: ")
		self.campo = int(input())
		
	def campoDeSaldo(self, saldo):
		print("O seu saldo eh: %s", saldo)	

	def campoDeSaque(self):
		print("Digite a quantidade a ser sacada: ")
		saque = int(input())
		return saque