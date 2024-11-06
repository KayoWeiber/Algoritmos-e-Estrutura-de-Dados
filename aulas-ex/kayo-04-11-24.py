class musica:
    def __init__(self,msc):
        self.musica=msc
        self.proximo=None
        self.anterior=None
class Playlist:
    def __init__(self):
        self.cabeca=None
        self.atual=None
    def adicionar_musica(self,titulo): #mudar
        nova_musica=musica(titulo)
        if not self.cabeca:
            self.cabeca=nova_musica
            self.atual=nova_musica
            print(f"\nA Musica \"{titulo}\" incluido na lista")
            
        else:
            atual=self.cabeca
            while atual.proximo: #Se atual tem proximo
                atual=atual.proximo #Atual vai virar o próximo
            atual.proximo=nova_musica #se não entrar no else vira a musica atual
            nova_musica.anterior=atual
            print(f"\nA Musica \"{titulo}\" incluido na lista")
            
    def alterar_titulo(self,titulo_atual,novo_titulo):
        if not self.cabeca:
            print("A Playlist está vazia")
            return
        atual=self.cabeca
        while atual:
            if atual.musica==titulo_atual:
                atual.musica=novo_titulo
                print(f"\nA Musica {titulo_atual} foi alterado para {novo_titulo}")
                return
            atual=atual.proximo
        print(f"A Musica {titulo_atual} não foi encontrado na playlist")
        
    def exibir_playlist(self):
        if not self.cabeca:
            print("\nA Playlist está vazia")
            return
        atual=self.cabeca
        elementos=[]
        while atual:
            elementos.append(atual.musica)
            atual=atual.proximo
        print("\nPlaylist atual:", " - ".join(map(str,elementos)))
        
    def remover_musica(self,musica):
        if not self.cabeca:
            print("\nA Playlist está vazia")
            return
        atual=self.cabeca
        while atual:
            if atual.musica==musica:
                if atual.anterior:
                    atual.anterior.proximo=atual.proximo
                else:
                    self.cabeca=atual.proximo
                if atual.proximo:
                    atual.proximo.anterior=atual.anterior
                print(f"\nA musica {musica} foi removido da playlist")
                return
            atual=atual.proximo
        print(f"\nA Musica {musica} não foi encontrado na playlist")
    def tocar_proxima(self):
        if self.atual and self.atual.proximo:
            self.atual=self.atual.proximo
            print(f"\nMúsica tocando agora: {self.atual.musica}")
        else:
            print("\nNão há nenhuma música a seguir.")

    def tocar_anterior(self):
        if self.atual and self.atual.anterior:
            self.atual=self.atual.anterior
            print(f"\nMúsica tocando agora: {self.atual.musica}")
        else:
            print("\nNão há nenhuma música anterior.")
'''       
#musica_teste=musica("Alo ambev")
playlist_teste=Playlist()
#musica_teste()
playlist_teste.adicionar_musica("Coração gelado")
playlist_teste.exibir_playlist()
playlist_teste.adicionar_musica("Alo Ambev")
playlist_teste.alterar_titulo("Alo Ambev","Alo Imperio")
playlist_teste.exibir_playlist()
playlist_teste.adicionar_musica("Forró boys")
playlist_teste.exibir_playlist()
playlist_teste.remover_musica("Forró boys")
playlist_teste.exibir_playlist()
playlist_teste.tocar_proxima()
playlist_teste.tocar_proxima()
''' 
playlist=Playlist()
while True:
    try:
        menu_principal=int(input("\nMenu:\n1-Adicionar uma nova música\n2-Remover uma música\n3-Alterar o título de uma música\n4-Tocar a próxima música\n6-Tocar a música anterior\n6-Exibir todas as músicas na playlist.\n0-Sair\nDigite o Valor que deseja executar: "))
        if menu_principal>6 or menu_principal<0:
            print("O Valor digitado não é válido")
        else:
            if menu_principal==1:
                musica_add=str(input("Digite a música que deseja adicionar a Playlist: "))
                playlist.adicionar_musica(musica_add)
                #playlist.exibir_playlist()
            elif menu_principal==2:
                playlist.exibir_playlist()
                musica_remov=str(input("Digite a música que deseja remover da Playlist: "))
                playlist.remover_musica(musica_remov)
            elif menu_principal==3:
                playlist.exibir_playlist()
                musica_altA=str(input("Digite o titulo que deseja alterar: "))
                musica_altB=str(input("Digite o novo Titulo que deseja adicionar: "))
                playlist.alterar_titulo(musica_altA,musica_altB)
                
            elif menu_principal==4:
                playlist.tocar_proxima()
            elif menu_principal==5:
                playlist.tocar_anterior()
            elif menu_principal==6:
                playlist.exibir_playlist()
            else:
                print("Programa finalizado")
                break
    
    except ValueError:
        print("Valor inválido, tente novamente!")
