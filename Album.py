from ListaDobleCanciones import ListaDobleCancion
class NodeAlbum:
    def __init__(self,artista,album):
        self.artistaB = artista
        self.albumB = album
        self.nombreB = ListaDobleCancion()
        self.siguienteAlbum = None
        self.anteriorAlbum = None

    def getCancion(self):
        return self.nombreB
    
    def setCancion(self, nombre):
        self.nombreB = nombre
