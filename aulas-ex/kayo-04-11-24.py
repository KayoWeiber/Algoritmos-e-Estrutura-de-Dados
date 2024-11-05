class musica:
    def __init__(self,msc):
        self.musica=msc
        self.proximo=None
        self.anterior=None
class Playlist:
    def __init__(self):
        self.cabeca=None
    def adicionar_musica(self,musica): #mudar
        nova_musica=musica(musica)
        if not self.cabeca:
            self.cabeca=nova_musica
        else:
            atual=self.cabeca
            while atual.proximo: #Se atual tem proximo
                atual=atual.proximo #Atual vai virar o próximo
            atual.proximo=nova_musica #se não entrar no else vira a musica atual
            nova_musica.anterior=atual
            print(f"A Musica \"{musica}\" incluido na lista")
            
    def alterar_titulo(self,titulo_atual,novo_titulo):
        if not self.cabeca:
            print("A Playlist está vazia")
            return
        atual=self.cabeca
        while atual:
            if atual.musica==titulo_atual:
                atual.musica=novo_titulo
                print(f"A Musica {titulo_atual} foi alterado para {novo_titulo}")
                return
            atual=atual.proximo
        print(f"A Musica {titulo_atual} não foi encontrado na playlist")
        
    def exibir_playlist(self):
        if not self.cabeca:
            print("A Playlist está vazia")
            return
        atual=self.cabeca
        elementos=[]
        while atual:
            elementos.append(atual.musica)
            atual=atual.proximo
        print("Playlist atual:", " - ".join(map(str,elementos)))
        
    def remover_musica(self,musica):
        if not self.cabeca:
            print("A Playlist está vazia")
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
                print(f"A musica {musica} foi removido da playlist")
                return
            atual=atual.proximo
        print(f"A Musica {musica} não foi encontrado na playlist")
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