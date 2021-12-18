

#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------- Listas --------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

#------------------------------------------------------ Artista --------------------------------------------------------
class ListaDobleArtista:    
    def __init__(self):
        self.inicioArtista = None
        self.finalArtista = None                    
    
    def listarArtista(self, artista):  
        nuevoArtista = NodeTemp(artista)
        if self.inicioArtista is None:            
            self.inicioArtista = nuevoArtista
            self.finalArtista = self.inicioArtista
        else:            
            n = self.finalArtista  
            n.siguiente= nuevoArtista
            self.finalArtista = n.siguiente
            self.finalArtista.anterior = n
    
    def mostrarArtista(self):
        if self.inicioArtista is None:
            print("La lista esta vacía")            
        else:
            n = self.inicioArtista
            while n is not None:                
                yield n
                n = n.siguiente

    def mostrarArtistaFinal(self):
        if self.inicioArtista is None:
            print("La lista esta vacía")            
        else:
            n = self.finalArtista
            while n is not None:                
                yield n
                n = n.anterior
                
#------------------------------------------------------- Album --------------------------------------------------------
class ListaDobleAlbum:
    def __init__(self):
        self.inicioAlbum = None    
        self.finalAlbum = None 
        
    def listarAlbum(self,album):        
        nuevoAlbum = NodeTemp(album)     
        if self.inicioAlbum is None:            
            self.inicioAlbum = nuevoAlbum
            self.finalAlbum = self.inicioAlbum
        else:            
            m = self.finalAlbum  
            m.siguiente= nuevoAlbum
            self.finalAlbum = m.siguiente
            self.finalAlbum.anterior = m

    def mostrarAlbum(self):
        if self.inicioAlbum is None:
            print("La lista esta vacía")            
        else:
            m = self.inicioAlbum
            while m is not None:   
                yield m
                m = m.siguiente      

#------------------------------------------------------- Cancion --------------------------------------------------------
class ListaDobleCancion:
    def __init__(self):
        self.inicioCancion = None 
        self.finalCancion = None    

    def listarCancion(self,cancion):        
        nuevaCancion = NodeTemp(cancion)
         
        if self.inicioCancion is None:            
            self.inicioCancion = nuevaCancion
            self.finalCancion = self.inicioCancion
        else:            
            o = self.finalCancion  
            o.siguiente = nuevaCancion
            self.finalCancion = o.siguiente
            self.finalCancion.anterior = o

    def mostrarCancion(self):
        if self.inicioCancion is None:
            print("La lista esta vacía")            
        else:
            o = self.inicioCancion
            while o is not None:                  
                yield o
                o = o.siguiente

#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------- Clases --------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

#------------------------------------------------------- Artista --------------------------------------------------------
class NodeArtista:
    def __init__(self,artista):
        self.artistaA = artista 
        self.albumA = ListaDobleAlbum()  
    
    def setAlbum(self,album):
        self.existe = False
        for alb in self.albumA.mostrarAlbum():
            if alb.data.albumB == album:
                self.existe = True
                return alb
        if self.existe == False:
            return False
    
#------------------------------------------------------- Album --------------------------------------------------------
class NodeAlbum:
    def __init__(self,album,imagen):
        self.albumB = album
        self.imagenB = imagen
        self.cancionB = ListaDobleCancion()

    def setCancion(self,cancion):
        self.existe = False
        for canc in self.cancionB.mostrarCancion():
            if canc.data.nombreC == cancion:
                self.existe = True
                return canc
        if self.existe == False:
            return False
#------------------------------------------------------- Cancion --------------------------------------------------------
class NodeCancion:
    def __init__(self,nombre, ruta):
        self.nombreC = nombre
        self.rutaC = ruta

    def __str__(self):
        return "Cancion -> {}".format(self.nombreC,"",self.rutaC)
#------------------------------------------------------- Temporal --------------------------------------------------------

class NodeTemp:
    def __init__(self, data):
        self.data = data
        self.siguiente= None
        self.anterior = None

class Llenado:
    def __init__(self):
        self.listaArtistas = ListaDobleArtista()

    def agregarCancion(self, artista,album,imagen,ruta,nombre):
        art = artista
        alb = album
        img = imagen
        rut = ruta
        nom = nombre
        contenedor = self.Biblioteca(artista)
        if contenedor != False:
            artista = contenedor.data
            contenedor = artista.setAlbum(alb) 
            if contenedor != False:
                album = contenedor.data
                contenedor = album.setCancion(nombre)
                if contenedor != False:
                    print("La cancion {} ya existe en ese album y artista".format(contenedor.data.nombreC))
                else:
                    nuevaCancion = NodeCancion(nom,rut)
                    album.cancionB.listarCancion(nuevaCancion)
            else:
                nuevaCancion = NodeCancion(nom,rut)
                nuevoAlbum = NodeAlbum(alb,img)
                nuevoAlbum.cancionB.listarCancion(nuevaCancion) 
                artista.albumA.listarAlbum(nuevoAlbum)
        else:
            nuevaCancion = NodeCancion(nom,rut)
            nuevoAlbum = NodeAlbum(alb,img)
            nuevoAlbum.cancionB.listarCancion(nuevaCancion) 
            nuevoArtista = NodeArtista(art)
            nuevoArtista.albumA.listarAlbum(nuevoAlbum)
            self.listaArtistas.listarArtista(nuevoArtista)
    
    def Biblioteca(self, dato):
        self.existe = False
        for biblioteca in self.listaArtistas.mostrarArtista():
            if biblioteca.data.artistaA == dato:
                self.existe = True
                return biblioteca
        if self.existe == False:
            return False