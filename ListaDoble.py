class NodeArtista:
    def __init__(self,artista):
        self.artistaA = artista 
        self.albumA = ListaDobleAlbum()  
    
    def setAlbum(self,album):
        return self.albumA.listarAlbum(album)


class NodeAlbum:
    def __init__(self,album,imagen):
        self.albumB = album
        self.imagenB = imagen
        self.cancionB = ListaDobleCancion()

    def setCancion(self,cancion):
        return self.cancionB.listarCancion(cancion)


class NodeCancion:
    def __init__(self,nombre, ruta):
        self.nombreC = nombre
        self.rutaC = ruta

class NodeTemp:
    def __init__(self, data):
        self.data = data
        self.siguiente= None
        self.anterior = None

class ListaDobleArtista:    
    def __init__(self):
        self.inicioArtista = None                    
    
    def listarArtista(self, artista):  
        if self.inicioArtista is None:
            nuevoArtista = NodeTemp(artista)
            self.inicioArtista = nuevoArtista
            return    
        else:
            n = self.inicioArtista            
            while n.siguiente is not None:
                n = n.siguiente
            nuevoArtista = NodeTemp(artista)
            n.siguiente= nuevoArtista
            nuevoArtista.anterior = n  

    
    def mostrarArtista(self):
        if self.inicioArtista is None:
            print("La lista esta vacía")            
        else:
            n = self.inicioArtista
            while n is not None:            
                artista = n.data
                n = n.siguiente
                yield artista

class ListaDobleAlbum:
    def __init__(self):
        self.inicioAlbum = None     
        
    def listarAlbum(self,album):        
        if self.inicioAlbum is None:     
            nuevoAlbum = NodeTemp(album)       
            self.inicioAlbum = nuevoAlbum             
        else:      
            m = self.inicioAlbum
            while m.siguiente is not None:
                m = m.siguiente
            if m.siguiente != album:
                nuevoAlbum = NodeTemp(album)
                m.siguiente = nuevoAlbum
                nuevoAlbum.anterior = m

    def mostrarAlbum(self):
        if self.inicioAlbum is None:
            print("La lista esta vacía")            
        else:
            m = self.inicioAlbum
            while m is not None:            
                artista = m.data
                m = m.siguiente
                yield artista        
    
class ListaDobleCancion:
    def __init__(self):
        self.inicioCancion = None     

    def listarCancion(self,cancion):
        if self.inicioCancion is None:
            nuevaCancion = NodeTemp(cancion)
            self.inicioCancion = nuevaCancion
        o = self.inicioCancion
        while o.siguiente is not None:
            o = o.siguiente
        nuevaCancion = NodeTemp(cancion)
        o.siguiente = nuevaCancion
        nuevaCancion.anterior = o

    def mostrarAlbum(self):
        if self.inicioCancion is None:
            print("La lista esta vacía")            
        else:
            o = self.inicioCancion
            while o is not None:            
                artista = o.data
                o = o.siguiente
                yield artista

    