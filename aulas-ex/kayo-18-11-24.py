'''
fila=[]
while True:
    try:
        menu=int(input("\nMenu:\n1-Inserir elemento\n2-Remover elemento\n3-Verificar tamanho da lista\n4-Localicar elemento\n5-Verificar a posição do elemento\n6-sair\n Digite o item desejável:"))
        if menu<0 or menu>6:
            print("O válor digitado não é válido")
        else:
            if menu==1:
                elementoInser=int(input("Digite o número que deseja adicionar na fila: "))
                fila.append(elementoInser)
            elif menu==2:
                fila.pop(0)
                print("O primeiro elemento foi removido")
            elif menu==3:
                
                print(f"O tamanho da fila é: {len(fila)}")
            elif menu==4:
                elementoLoc=int(input("Digite o valor que deseja localizar posição:"))
                count=0
                for i,a in enumerate(fila):
                    if a==elementoLoc:
                        print(f"Posição:{i+1} - elemento {a}")
                    else:
                            count+=1
                if count==len(fila):
                    print("Item não encontrado")
                
            elif menu==5:
                for i,a in enumerate(fila):
                    print(f"Posição:{i+1} - elemento {a}")
            else:
                print("Programa finalizado")
                break      
    except ValueError:
        print("Valor inválido")
        
'''
class Hist:
    def __init__(self):
        self.dicio=[{}]
    def adicionar(self,id,url,timestamp):
        Historico={"id":id,"url":url,"timestamp":timestamp}
        self.dicio.append(Historico)
        print("Histórico atualizado")
    