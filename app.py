import tkinter
from tkinter.constants import FALSE, N, TRUE
import xml.etree.ElementTree as ET

class IG():
    ventana =  tkinter.Tk()
    ventana.title("IPCmusic")
    ventana.geometry("1100x700")
    #-----------------------------------------------------------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------------------
    #------------------------------------------------------ Frames ---------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------------------
    frame = tkinter.Frame(ventana)
    # Establece la posición del componente
    frame.place(x=35,y=85)
    # Color de fondo, background
    frame.config(bg="lightgrey")   
    # Podemos establecer un tamaño
    frame.config(width=1000,height=550)
    # Establece el ancho del borde 
    frame.config(bd=10)
    # Establece el tipo de relieve para el borde
    frame.config(relief="ridge")

    frameInfo = tkinter.Frame(frame)
    # Establece la posición del componente
    frameInfo.place(x=400,y=150)
    # Color de fondo, background
    frameInfo.config(bg="grey")   
    # Podemos establecer un tamaño
    frameInfo.config(width=500,height=250)
    # Establece el ancho del borde 
    frameInfo.config(bd=10)
    # Establece el tipo de relieve para el borde
    frameInfo.config(relief="ridge")

    frameAr = tkinter.Frame(ventana)
    # Establece la posición del componente
    frameAr.place(x=35,y=10)
    # Color de fondo, background
    frameAr.config(bg="lightgrey")   
    # Podemos establecer un tamaño
    frameAr.config(width=400,height=60)
    # Establece el ancho del borde 
    frameAr.config(bd=10)
    # Establece el tipo de relieve para el borde
    frameAr.config(relief="ridge")

    frameBu = tkinter.Frame(ventana)
    # Establece la posición del componente
    frameBu.place(x=450,y=10)
    # Color de fondo, background
    frameBu.config(bg="lightgrey")   
    # Podemos establecer un tamaño
    frameBu.config(width=585,height=60)
    # Establece el ancho del borde 
    frameBu.config(bd=10)
    # Establece el tipo de relieve para el borde
    frameBu.config(relief="ridge")

    frameIm = tkinter.Frame(frame)
    # Establece la posición del componente
    frameIm.place(x=55,y=65)
    # Color de fondo, background
    frameIm.config(bg="grey")   
    # Podemos establecer un tamaño
    frameIm.config(width=300,height=400)
    # Establece el ancho del borde 
    frameIm.config(bd=10)
    # Establece el tipo de relieve para el borde
    frameIm.config(relief="ridge")

    #-----------------------------------------------------------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------------------
    #------------------------------------------------------ Labels ---------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------------------
    Label1 = tkinter.Label(frameInfo, text="Canción")
    Label1.config(fg="white", bg="grey", font=("broadway 18 bold"))
    Label1.place(x=10,y=40)

    CANCION = "VALOR"

    Label1A = tkinter.Label(frameInfo, text=CANCION)
    Label1A.config(fg="white", bg="grey", font=("broadway 15 "))
    Label1A.place(x=150,y=45)

    Label2 = tkinter.Label(frameInfo, text="Artista")
    Label2.config(fg="white", bg="grey", font=("broadway 18 bold"))
    Label2.place(x=10,y=90)

    ARTISTA = "VALOR2"

    Label2A = tkinter.Label(frameInfo, text=ARTISTA)
    Label2A.config(fg="white", bg="grey", font=("broadway 15"))
    Label2A.place(x=150,y=95)

    Label3 = tkinter.Label(frameInfo, text="Album")
    Label3.config(fg="white", bg="grey", font=("broadway 18 bold"))
    Label3.place(x=10,y=140)

    ALBUM = "VALOR3"

    Label3A = tkinter.Label(frameInfo, text=ALBUM)
    Label3A.config(fg="white", bg="grey", font=("broadway 15"))
    Label3A.place(x=150,y=145)

    #-----------------------------------------------------------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------------------
    #------------------------------------------------------ Buttons --------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------------------

    def hola():
        print("Hola Mundo")

    img = tkinter.PhotoImage(file='anterior.png')
    img_label = tkinter.Label(image=img)
    boton1 = tkinter.Button(frame, image=img, command = hola, borderwidth=0, bg="lightgrey")
    boton1.place(x=500,y=420)
    boton1.config(width=75, height=75)

    img2 = tkinter.PhotoImage(file='siguiente.png')
    img_label2 = tkinter.Label(image=img2)
    boton2 = tkinter.Button(frame, image=img2, command = hola, borderwidth=0, bg="lightgrey")
    boton2.place(x=700,y=420)
    boton2.config(width=75, height=75)

    img3 = tkinter.PhotoImage(file='play.png')
    img_label3 = tkinter.Label(image=img3)
    boton3 = tkinter.Button(frame, image=img3, command = hola, borderwidth=0, bg="lightgrey")
    boton3.place(x=500,y=50)
    boton3.config(width=75, height=75)

    img4 = tkinter.PhotoImage(file='pausa.png')
    img_label4 = tkinter.Label(image=img4)
    boton4 = tkinter.Button(frame, image=img4, command = hola, borderwidth=0, bg="lightgrey")
    boton4.place(x=600,y=50)
    boton4.config(width=75, height=75)

    img5 = tkinter.PhotoImage(file='stop.png')
    img_label5 = tkinter.Label(image=img5)
    boton5 = tkinter.Button(frame, image=img5, command = hola, borderwidth=0, bg="lightgrey")
    boton5.place(x=700,y=50)
    boton5.config(width=75, height=75)
    
    boton6 = tkinter.Button(frameAr,text="Archivo", fg="white",font=("broadway 12 bold"), command = hola, borderwidth=0, bg="grey")
    boton6.place(x=25,y=5)
    boton6.config(width=12, height=1)

    boton7 = tkinter.Button(frameAr,text="Reporte", fg="white",font=("broadway 12 bold"), command = hola, borderwidth=0, bg="grey")
    boton7.place(x=205,y=5)
    boton7.config(width=12, height=1)

    busqueda = tkinter.StringVar()
    txtA = tkinter.Entry(frameBu, textvariable=busqueda)
    txtA.place(x=43,y=0)
    txtA.config(width=86)
    
    
    def pn(valor):        
        print(valor)

    img8 = tkinter.PhotoImage(file='lupa.png')
    img_label8 = tkinter.Label(image=img8)
    boton8 = tkinter.Button(frameBu, image=img8, command = pn(busqueda.get()), borderwidth=0, bg="white")
    boton8.place(x=0,y=0)
    boton8.config(width=40, height=40)

    #-----------------------------------------------------------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------------------
    #------------------------------------------------------- Entry ---------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------------------

    


    ventana.config(cursor="arrow")
    ventana.config(bg="grey")
    ventana.config(bd=15)
    ventana.config(relief="ridge")
    ventana.mainloop() 

    #-----------------------------------------------------------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------------------
    #------------------------------------------------------- Listas --------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------------------

#------------------------------------------------------- Artista --------------------------------------------------------

class NodeArtista:
    def __init__(self,artista):
        self.artistaA = artista    
        self.albumA = ListaDobleAlbum()
        self.nrefA = None
        self.prefA = None

class ListaDobleArtista:
    def __init__(self):
        self.start_nodeA = None        
    
    def listarArtista(self, artista):  
        if self.start_nodeA is None:
            new_node = NodeArtista(artista)
            self.start_nodeA = new_node
            return       
        elif artista == self.start_nodeA.artistaA:
            repetido = TRUE
        else:
            n = self.start_nodeA            
            while n.nrefA is not None:
                n = n.nrefA
            if n.artistaA != artista:
                new_node = NodeArtista(artista,Album.start_nodeB.albumB)
                n.nrefA = new_node
                new_node.prefA = n
                
    def mostrar(self):
        if self.start_nodeA is None:
            print("La agenda esta vacía")
            return
        else:
            n = self.start_nodeA
            while n is not None:
                print(n.artistaA,"",n.albumA)    
                n = n.nrefA

Artista = ListaDobleArtista()
#-------------------------------------------------------- Album --------------------------------------------------------

class NodeAlbum:
    def __init__(self,artista,album):
        self.artistaB = artista
        self.albumB = album
        self.nombreB = ListaDobleCancion()
        self.nrefB = None
        self.prefB = None

class ListaDobleAlbum:
    def __init__(self):
        self.start_nodeB = None

    def listarAlbum(self,artista, album):
        if self.start_nodeB is None:
            new_nodeB = NodeAlbum(artista, album)
            self.start_nodeB = new_nodeB
            return
        m = self.start_nodeB
        while m.nrefB is not None:
            m = m.nrefB
        new_nodeB = NodeAlbum(artista, album)
        m.nrefB = new_nodeB
        new_nodeB.prefB = m
    
    def mostrarB(self):
        if self.start_nodeB is None:
            print("La agenda esta vacía")
            return
        else:
            n = self.start_nodeB
            while n is not None:
                print(n.artistaB,"",n.albumB)    
                n = n.nrefB

Album = ListaDobleAlbum()
#-------------------------------------------------------- Cancion --------------------------------------------------------

class NodeCancion:
    def __init__(self,imagen,ruta, nombre):
        self.imagenC = imagen
        self.rutaC = ruta
        self.imagenC = nombre
        self.nrefC = None
        self.prefC = None

class ListaDobleCancion:
    def __init__(self):
        self.start_nodeC = None

    def listarCancion(self,imagen, ruta, nombre):
        if self.start_nodeC is None:
            new_nodeC = NodeCancion(imagen,ruta, nombre)
            self.start_nodeC = new_nodeC
            return
        o = self.start_nodeC
        while o.nrefC is not None:
            o = o.nrefC
        new_nodeC = NodeCancion(imagen,ruta, nombre)
        o.nrefC = new_nodeC
        new_nodeC.prefC = o

Cancion = ListaDobleCancion()
#--------------------------------------------------------- XML --------------------------------------------------------

def impA():
    contenido = open("biblioteca.xml").read()
    ListArtista = ListaDobleArtista()
    biblioteca = ET.fromstring(contenido)
    for biblio in biblioteca.iter("biblioteca"):    

        for alb in biblio.iter("album"):
            artista = ""
            album = ""
            for ar,al in zip(alb.iter("artista"),alb.iter("album")):        
                artista += ar.text
                album += al.text
            Album.listarAlbum(artista,album)   

        for art in biblio.iter("artista"):
            artista = ""
            for ar in zip(art.iter("artista")):                
                artista += art.text
            Artista.listarArtista(artista)
            

def impB():
    impA()
    contenido = open("biblioteca.xml").read()
    ListaAlbum = ListaDobleAlbum()
    biblioteca = ET.fromstring(contenido)
    for biblio in biblioteca.iter("biblioteca"):
        for art in biblio.iter("album"):
            album = ""
            for al in zip(art.iter("album")):        
                album += art.text
            Album.listarAlbum(album)

def impC():
    contenido = open("biblioteca.xml").read()
    ListArtista = ListaDobleArtista()
    ListaAlbum = ListaDobleAlbum()
    ListaCancion = ListaDobleCancion()
    biblioteca = ET.fromstring(contenido)
    for biblio in biblioteca.iter("biblioteca"):
        for art in biblio.iter("artista"):
            artista = ""
            album = ""
            imagen = ""
            ruta = ""
            nombre = ""
            for ar,al,im,ru,no in zip(art.iter("artista"),art.iter("album"),art.iter("imagen"),art.iter("ruta"),art.iter("nombre")):                
                artista += ar.text
                album += al.text
                imagen += im.text
                ruta += ru.text
                nombre += no.text 
            Artista.listarArtista(artista)
            Album.listarAlbum(album)
            Cancion.listarCancion(imagen,ruta,nombre)



Salir = False
opcion = 0

while not Salir:
    print("1. Importar contactos")
    print("2. Mostar Datos")
    print("3. Salir")
    print("--------------------------------------")

    menu = (input("Opcion: "))
    if menu.isdigit():
        menu = int(menu)
        if menu == 1:           
            impA()
        elif menu == 2:
            Artista.mostrar()
        elif menu == 3:
            exit()
    else:
            print("Debe ingresar una opcion valida ")