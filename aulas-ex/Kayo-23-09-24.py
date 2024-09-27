#criando classes
"""class myclass:
    x=5
p1=myclass()
print(p1.x)

"""

"""class pessoas:
    Nome="Kayo"
    peso=85.3
    cpf=454445454
    naturalidade="Ceara"
    altura="1,78"
rh=pessoas()
print(rh.Nome)
print(rh.cpf)
print(rh.peso)
print(rh.naturalidade)
print(rh.altura) 


class automovel:
    def __init__(self, cor,modelo,ano,marca,potencia):
        self.cor=cor
        self.modelo=modelo
        self.ano=ano
        self.marca=marca
        self.potencia=potencia
p1=automovel("preto",'civic',2020,'hyundai',500)
print("ANO:",p1.ano)
print("COR:",p1.cor)
print("MARCA:",p1.marca)
print("MODELO:",p1.modelo)
print("POTENCIA:",p1.potencia)

#1° atividade
class moto:
    def __init__(self,modelo,ano,cor,cilindrada):
        self.cor=cor
        self.modelo=modelo
        self.ano=ano
        self.cilindrada=cilindrada
p1=moto("Hornet",2012,"preta",600)
p2=moto("CB300",2019,"branca",300)
print("ANO:",p1.ano)
print("COR:",p1.cor)
print("MODELO:",p1.modelo)
print("CILINDRADA:",p1.cilindrada)
print()
print("ANO:",p2.ano)
print("COR:",p2.cor)
print("MODELO:",p2.modelo)
print("CILINDRADA:",p2.cilindrada)


#2° atividade
class moto:
    def __init__(self,modelo,ano,cor,cilindrada):
        self.cor=cor
        self.modelo=modelo
        self.ano=ano
        self.cilindrada=cilindrada
    def acerela(self):
        print(f"Acelerando minha {self.modelo}")
p1=moto("Hornet",2012,"preta",600)
print("ANO:",p1.ano)
print("COR:",p1.cor)
print("MODELO:",p1.modelo)
print("CILINDRADA:",p1.cilindrada),print()
p1.acerela()

p2=moto("CB300",2019,"branca",300)
print()
print("ANO:",p2.ano)
print("COR:",p2.cor)
print("MODELO:",p2.modelo)
print("CILINDRADA:",p2.cilindrada)
p2.acerela()


class tv:
    def __init__(self,volume,canal,status):
        self.volume=volume
        self.canal=canal
        self.status=status
    def aumentarvolume(self):
        if self.volume>=0 and self.volume<=100:
            self.volume+=1  
            print(self.volume)     
    def diminuirvolume(self):
        if self.volume>=0 and self.volume<=100:
            self.volume-=1
            print(self.volume)
    def alterarcanal(self):
        if self.canal>=0 and self.canal<=100:
            self.canal+=1
            print(self.canal)
    def liga_desliga(self):
        if self.status==True:
            self.status==False
            print("Tv desligada")
        else:
            self.status==True 
            print("Tv ligada")
estado=tv(50,5,False)
while True:
    controle=int(input("Controle\n1-Ligar/desligar\n2-aumentar volume\n3-diminuir volume\n4-mudar canal\n100-sair do programa\n"))
    if controle==2:
            estado.aumentarvolume()
    elif controle==3:
            estado.diminuirvolume()
    elif controle==4:
           estado.alterarcanal()
    elif controle==1:
            estado.liga_desliga()
    elif controle==100:
            break
    print()

    

#1° atividade
class pessoa:
    def __init__(self,nome,sexo,dt_nascimento,rg):
        self.nome=nome
        self.sexo=sexo
        self.dt_nascimento=dt_nascimento
        self.rg=rg
p1=pessoa("Kayo","Masculino","10/03/2005","732848733")
p2=pessoa("Jorge","Feminino","01/09/1984","3748738")
print("Pessoa 1\n",
      "Nome:",p1.nome,"\n"
      "Sexo:",p1.sexo, "\n"
      "Data de nascimento:",p1.dt_nascimento,"\n"
      "RG",p1.rg,"\n")
print("Pessoa 2\n",
      "Nome:",p2.nome,"\n"
      "Sexo:",p2.sexo, "\n"
      "Data de nascimento:",p2.dt_nascimento,"\n"
      "RG",p2.rg,"\n")

#2° atividade
class moto:
    def __init__(self,modelo,ano,cor,cilindrada):
        self.cor=cor
        self.modelo=modelo
        self.ano=ano
        self.cilindrada=cilindrada
p1=moto("Hornet",2012,"preta",600)
p2=moto("CB300",2019,"branca",300)
print("ANO:",p1.ano)
print("COR:",p1.cor)
print("MODELO:",p1.modelo)
print("CILINDRADA:",p1.cilindrada)
print()
print("ANO:",p2.ano)
print("COR:",p2.cor)
print("MODELO:",p2.modelo)
print("CILINDRADA:",p2.cilindrada)


##3° atividade
class pessoa:
    def __init__(self,nome,sexo,dt_nascimento,rg):
        self.nome=nome
        self.sexo=sexo
        self.dt_nascimento=dt_nascimento
        self.rg=rg
    def myfunction_saudação(self):
        print(f"olá {self.nome}, seja bem vindo!")
    def myfunction_despedida(self):
        print(f"Tchau {self.nome}, até a próxima!\n")
p1=pessoa("Kayo","Masculino","10/03/2005","732848733")
p2=pessoa("Jorge","Feminino","01/09/1984","3748738")

p1.myfunction_saudação()
print("Pessoa 1\n",
      "Nome:",p1.nome,"\n"
      "Sexo:",p1.sexo, "\n"
      "Data de nascimento:",p1.dt_nascimento,"\n"
      "RG",p1.rg,"\n")
p1.myfunction_despedida()


p2.myfunction_saudação()
print("Pessoa 2\n",
      "Nome:",p2.nome,"\n"
      "Sexo:",p2.sexo, "\n"
      "Data de nascimento:",p2.dt_nascimento,"\n"
      "RG",p2.rg,"\n")
p2.myfunction_despedida()

"""
#4° atividade
class moto:
    def __init__(self,modelo,ano,cor,cilindrada):
        self.cor=cor
        self.modelo=modelo
        self.ano=ano
        self.cilindrada=cilindrada
    def ligar_moto(self):
        print(f"{self.modelo} ligando.")
    def desligar_moto(self):
        print(f"{self.modelo} desligando.")
        
p1=moto("Hornet",2012,"preta",600)
p2=moto("CB300",2019,"branca",300)

p1.ligar_moto()
print("ANO:",p1.ano)
print("COR:",p1.cor)
print("MODELO:",p1.modelo)
print("CILINDRADA:",p1.cilindrada)
p1.desligar_moto()

print()
p2.ligar_moto()
print("ANO:",p2.ano)
print("COR:",p2.cor)
print("MODELO:",p2.modelo)
print("CILINDRADA:",p2.cilindrada)
p2.desligar_moto()
