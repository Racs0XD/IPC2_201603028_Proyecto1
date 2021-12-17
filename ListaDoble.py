class NodeArtista:
    def __init__(self,artista):
        self.artistaA = artista 
        self.albumA = NodeAlbum("","")
        self.siguienteArtista = None
        self.anteriorArtista = None    
    
    def getAlbum(self):
        return self.albumA


class NodeAlbum:
    def __init__(self,artista,album):
        self.artistaB = artista
        self.albumB = album
        self.nombreB = NodeCancion("","","","","")
        self.siguienteAlbum = None
        self.anteriorAlbum = None

    def getCancion(self):
        return self.nombreB
    
    def setCancion(self, nombre):
        self.nombreB = nombre
    


class NodeCancion:
    def __init__(self,nombre,album,artista, imagen, ruta):
        self.nombreC = nombre
        self.albumC = album
        self.artistaC = artista
        self.imagenC = imagen
        self.rutaC = ruta
        
        self.siguienteCancion = None
        self.anteriorCancion = None



class ListaDoble:    
    def __init__(self):
        self.inicioArtista = None    
        self.inicioAlbum = None    
        self.inicioCancion = None                  
    
    def listarArtista(self, artista):  
        if self.inicioArtista is None:
            nuevoArtista = NodeArtista(artista)
            self.inicioArtista = nuevoArtista
            return    
        else:
            n = self.inicioArtista            
            while n.siguienteArtista is not None:
                n = n.siguienteArtista
            if n.artistaA != artista:
                nuevoArtista = NodeArtista(artista)
                n.siguienteArtista = nuevoArtista
                nuevoArtista.anteriorArtista = n  

    
    
    def set(self, album):
        self.albumA = album 
    
    def getAlbum(self):
        return self.albumA

    def getArtista(self, artista):
        n = self.inicioArtista
        while n is not None:
            if n.artistaA == artista:
                return 
            n = n.siguienteArtista
        return None
    
    def mostrar(self):
        if self.inicioArtista is None:
            print("La agenda esta vacía")
            return
        else:
            n = self.inicioArtista
            while n is not None:
                print(n.artistaA,"",n.albumA)    
                n = n.siguienteArtista       

    def listarAlbum(self,artista, album):        
        if self.inicioAlbum is None:     
            nuevoAlbum = NodeAlbum(artista, album)       
            self.inicioAlbum = nuevoAlbum             
        else:      
            m = self.inicioAlbum
            while m.siguienteAlbum is not None:
                m = m.siguienteAlbum
            if m.siguienteAlbum != album:
                nuevoAlbum = NodeAlbum(artista, album)
                m.siguienteAlbum = nuevoAlbum
                nuevoAlbum.anteriorAlbum = m
        
    def mostrarB(self):
        if self.inicioAlbum is None:
            print("La agenda esta vacía")
            return
        else:
            n = self.inicioAlbum
            while n is not None:
                print(n.artistaB,"",n.albumB)    
                n = n.siguienteAlbum

    

    def listarCancion(self,nombre,album,artista,imagen,ruta,):
        if self.inicioCancion is None:
            nuevaCancion = NodeCancion(nombre,album,artista,imagen,ruta)
            self.inicioCancion = nuevaCancion
        o = self.inicioCancion
        while o.siguienteCancion is not None:
            o = o.siguienteCancion
        nuevaCancion = NodeCancion(nombre,album,artista,imagen,ruta)
        o.siguienteCancion = nuevaCancion
        nuevaCancion.anteriorCancion = o

    def mostrarCancion(self):
        if self.inicioCancion is None:
            print("La lista esta vacía")
            return
        else:
            n = self.inicioCancion
            while n is not None:
                print(n.nombreC,"",n.albumC,"",n.artistaC,"",n.imagenC,"",n.rutaC)    
                n = n.siguienteCancion
    


    def mostrarBiblioteca(self):        
        if self.inicioArtista is None:
            print("La lista esta vacía")
            return
        else:
            a = self.inicioArtista
            while a is not None:
                b = self.inicioAlbum
                while b is not None:
                    if a.artistaA == b.artistaB:                        
                        if a.albumA is None:
                            a.albumA = b.albumB
                        else:
                            a.albumA.siguienteAlbum = b.albumB   
                        c = self.inicioCancion
                        while c is not None:
                            if a.artistaA == c.artistaC and b.albumB == c.albumC:
                                b.nombreB = (c.nombreC,c.albumC,c.artistaC,c.imagenC,c.rutaC)                            
                            c = c.siguienteCancion
                    b = b.siguienteAlbum
                print(a.artistaA,"",str(a.albumA))      
                a = a.siguienteArtista