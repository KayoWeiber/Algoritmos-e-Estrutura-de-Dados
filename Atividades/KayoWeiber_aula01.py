"""
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
#2° atividade
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