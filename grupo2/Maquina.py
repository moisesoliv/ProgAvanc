#!/usr/bin/python
#-*- coding: utf-8 -*-

class Maquina:
    def __init__(self):
        self.saldoDaMaquina = None
        self.cartao = Cartao()
        self.view = View()

    def monitoraCartao(self, ):
        print("Insira cartao na maquina!")
        card = str(input())
        if card == cartao.id(card):
            print("Cartao aceito")

    def inputSenhaUser(self, ):
        view.campoDeSenha()

    def login(self, valorDeSaque):
        login.verificaSenha()
        login.atualizaSenha()
        login.validaCartao()

    def lancaMenuDeOpcoes(self, valorDeSaque):
        view.botaoCancela()
        view.botaoSaque()
        view.botaoSaldo()

    def opcaoSaldo(self, ):
        cartao.campoDeSaldo()

    def verificaSaldo(self, ):
        cartao.enviaSaldo()

    def opcaoSaque(self, ):
        login.verificaSenha()
    def comparaSaldo():
        if saldoDaMaquina-campoDeSaldo > 0:
            print("Saldo disponivel")
        else print("Saldo indisponivel")
    def ejetaValor():
        print("Recolhar o valor")
    def opcaoCancela():
        if botaoCancela == True:
            print("operação cancelada, retornando a tela inicial")

