'''
#ex01
class cachorro:
    def __init__(self,nome,idade):
        self.nome=nome
        self.idade=idade
    def latir(self):
        print(f"{self.nome} está latindo!")
cachorro1=cachorro("Belinha",4)
print(cachorro1.nome)
print(cachorro1.idade)
cachorro1.latir()

#ex02
class Retângulo:
    def __init__(self,largura,altura):
        self.largura=largura
        self.altura=altura
    def calcular_area(self):
        area=self.largura * self.altura
        print(area)
dados=Retângulo(4,8)
dados.calcular_area()
'''
#ex03
class ContaBancaria:
    def __init__(self,titular,saldo):
        self.titular=titular
        self.saldo=saldo
    def depositar_valor(self,depositar):
        self.saldo+=depositar
        print(f"Seu depósito de {depositar} foi realizado com sucesso, seu novo!")
    def sacar_valor(self,sacar):
        if sacar<=self.saldo:
            self.saldo-=sacar
            print(f"Seu saque de {sacar} foi realizado com sucesso, seu novo!")
        else:
            print("Saldo insuficiente.")   
try:
    conta_nome=str(input("Digite o nome da conta: "))
    conta_saldo=float(input("Digite o saldo da conta: "))
except ValueError:
    print("Valor inválido, digite os dados novamente")
while True:
    try:
        dados=ContaBancaria(conta_nome,conta_saldo)
        while True:
            menu=int(input("Menu:\n1-Depositar\n2-sacar\n3-Sair\nDigite sua escolhar: "))
            if menu>3 or menu<0:
                print("Valor inválido, digite um valor válido")
            else:
                if menu==1:
                    valor=float(input("Digite o valor que desejar: "))
                    dados.depositar_valor(valor)
                    print(f"Seu valor atual é de R${dados.saldo:.2f} ")
                elif menu==2:
                    valor=float(input("Digite o valor que desejar: "))
                    dados.sacar_valor(valor)
                    print(f"Seu valor atual é de R${dados.saldo:.2f} ")    
                else:
                    break
        break      
    except ValueError:
        print("Valor inválido, digite os dados novamente")         
print("Programa finalizado!")