import tkinter as tk
from tkinter import ttk, messagebox, font
from PIL import Image, ImageTk
import datetime
from config import COLOR_BARRA_SUPERIOR, COLOR_MENU_LATERAL, COLOR_CUERPO_PRINCIPAL, COLOR_MENU_CURSOR_ENCIMA
import util.util_ventana as util_ventana
import util.util_imagenes as util_img
import random

class Autor:
    def __init__(self, equipo, entrenador):
        self.equipo = equipo
        self.entrenador = entrenador
        self.categorias = []

    def agregar_categoria(self, categoria):
        self.categorias.append(categoria)

    def mostrar_info(self):
        return f"Equipo: {self.equipo}, Entrenador: {self.entrenador}"


class Categoria:
    def __init__(self, nombre, edad, posicion):
        self.nombre = nombre
        self.edad = edad
        self.posicion = posicion

    def mostrar_info(self):
        return f"Jugador: {self.nombre}, Edad: {self.edad}, Posición: {self.posicion}"

class Libro:
    def __init__(self, equipo_local, equipo_visitante, estadio):
        self.equipo_local = equipo_local
        self.equipo_visitante = equipo_visitante
        self.estadio = estadio
        self.resultado = None

    def mostrar_partido(self):
        return f"Partido: {self.equipo_local} vs {self.equipo_visitante} en {self.estadio}."

    def jugar_partido(self):
        resultados_posibles = ["Victoria", "Empate", "Derrota"]
        self.resultado = random.choice(resultados_posibles)

    def mostrar_resultado(self):
        if self.resultado:
            return f"Resultado: {self.resultado}"
        else:
            return "El partido no ha sido jugado aún"

class Usuario:
    def __init__(self, nombre, pais=None, anio_fundacion=None):
        self.nombre = nombre
        self.pais = pais
        self.anio_fundacion = anio_fundacion
        self.equipos = []  # Lista para almacenar equipos

    def agregar_equipo(self, equipo):
        self.equipos.append(equipo)

    def mostrar_info(self):
        return f"Equipo: {self.nombre}, País: {self.pais}, Año de fundación: {self.anio_fundacion}"



class Prestamo:
    def __init__(self, libro, usuario, fecha_prestamo, fecha_devolucion=None):
        self.libro = libro
        self.usuario = usuario
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion

    def mostrar_info(self):
        return (f"Préstamo - Libro: {self.libro.titulo}, Usuario: {self.usuario.nombre}, "
                f"Fecha de préstamo: {self.fecha_prestamo}, Fecha de devolución: {self.fecha_devolucion}")

class Biblioteca:
    def __init__(self):
        self.usuarios = []
        self.prestamos = []
        self.autores = []
        self.categorias = []
        self.libros = []

    def registrar_libro(self, libro):
        self.libros.append(libro)

    def registrar_grupo(self, grupo):
        self.prestamos.append(grupo)

    def realizar_prestamo(self, libro, usuario, fecha_prestamo):
        prestamo = Prestamo(libro, usuario, fecha_prestamo)
        self.prestamos.append(prestamo)

    def generar_fixture(self):
        if not self.libros:
            return "No hay partidos programados."
        
        fixture = []
        for libro in self.libros:
            partido = libro.mostrar_partido()
            fixture.append(partido)
        return "\n".join(fixture)


    def mostrar_autores(self):
        if not self.autores:
            return "No hay autores registrados."
        return "\n".join(autor.mostrar_info() for autor in self.autores)
    
    def registrar_equipo(self, equipo):
        self.usuarios.append(equipo)

    def registrar_categoria(self, categoria):
        self.categorias.append(categoria)
        
    def mostrar_categorias(self):
        if not self.categorias:
            return "No hay categorías registradas."
        return "\n".join(categoria.mostrar_info() for categoria in self.categorias)

    def mostrar_equipos(self):
        if not self.usuarios:  # Cambiar 'usuarios' a 'equipos'
            return "No hay equipos registrados."
        return "\n".join(usuario.mostrar_info() for usuario in self.usuarios)
    
class FormularioMaestroDesign(tk.Tk):
    def __init__(self):
        super().__init__()
        self.biblioteca = Biblioteca()
        self.init_data()
        self.logo = util_img.leer_imagen("imagenes/logo.png", (360, 460))
        self.perfil = util_img.leer_imagen("imagenes/Perfil.png", (100, 100))
        self.config_window()
        self.paneles()
        self.controles_barra_superior()        
        self.controles_menu_lateral()
        self.controles_cuerpo()
    
    def init_data(self):
        autores = [
            Autor("Barcelona", "Guardiola"),
            Autor("Real Madrid", "Zidane"),
            Autor("Manchester United", "Ferguson"),
            Autor("Liverpool", "Klopp"),
            Autor("Juventus", "Allegri"),
            Autor("Paris Saint-Germain", "Tuchel"),
            Autor("Bayern Munich", "Flick"),
            Autor("Chelsea", "Mourinho"),
            Autor("Atletico Madrid", "Simeone"),
            Autor("AC Milan", "Ancelotti")
        ]

        categorias = [
            Categoria("Lionel Messi", "35", "Delantero"),
            Categoria("Cristiano Ronaldo", "38", "Delantero"),
            Categoria("Neymar Jr.", "32", "Delantero"),
            Categoria("Kylian Mbappe", "25", "Delantero"),
            Categoria("Luka Modric", "38", "Centrocampista"),
            Categoria("Mohamed Salah", "31", "Delantero"),
            Categoria("Kevin De Bruyne", "32", "Centrocampista"),
            Categoria("Robert Lewandowski", "35", "Delantero"),
            Categoria("Sergio Ramos", "37", "Defensa"),
            Categoria("Virgil van Dijk", "32", "Defensa"),
            Categoria("Eden Hazard", "33", "Delantero"),
            Categoria("Karim Benzema", "36", "Delantero"),
            Categoria("Paul Pogba", "31", "Centrocampista"),
            Categoria("Antoine Griezmann", "33", "Delantero"),
            Categoria("Harry Kane", "30", "Delantero"),
            Categoria("Erling Haaland", "23", "Delantero"),
            Categoria("Raheem Sterling", "29", "Delantero"),
            Categoria("Sadio Mane", "32", "Delantero"),
            Categoria("Bruno Fernandes", "29", "Centrocampista"),
            Categoria("Zlatan Ibrahimovic", "42", "Delantero")

        ]

        libros = [
            Libro("Real Madrid", "Barcelona", "Bernabéu"),
            Libro("Manchester United", "Liverpool", "Old Trafford"),
            Libro("Bayern Munich", "Juventus", "Allianz Arena"),
            Libro("Paris Saint-Germain", "Chelsea", "Parc des Princes"),
            Libro("Manchester City", "Atlético de Madrid", "Etihad Stadium"),
            Libro("Barcelona", "Real Madrid", "Camp Nou"),
            Libro("Liverpool", "Manchester United", "Anfield"),
            Libro("Juventus", "Bayern Munich", "Juventus Stadium"),
            Libro("Chelsea", "Paris Saint-Germain", "Stamford Bridge"),
            Libro("Atlético de Madrid", "Manchester City", "Wanda Metropolitano")
        ]


        for autor in autores:
            for categoria in categorias:
                autor.agregar_categoria(categoria)

        for autor in autores:
            self.biblioteca.autores.append(autor)
            
        for libro in libros:
            self.biblioteca.registrar_libro(libro)
        usuarios = [
            Usuario("Barcelona", "España", "1899"),
            Usuario("Real Madrid", "España", "1902"),
            Usuario("Manchester United", "Inglaterra", "1878"),
            Usuario("Liverpool", "Inglaterra", "1892"),
            Usuario("Juventus", "Italia", "1897"),
            Usuario("Paris Saint-Germain", "Francia", "1970"),
            Usuario("Bayern Munich", "Alemania", "1900"),
            Usuario("Chelsea", "Inglaterra", "1905"),
            Usuario("Atletico Madrid", "España", "1903"),
            Usuario("AC Milan", "Italia", "1899")

        ]
        
        
        for categoria in categorias:
            self.biblioteca.registrar_categoria(categoria)
        
        for usuario in usuarios:
            self.biblioteca.registrar_equipo(usuario)
            
        for autor in autores:
                for categoria in categorias:
                    autor.agregar_categoria(categoria)
                    
    # Agregar grupos predeterminados
        grupoA = Usuario("Grupo A")
        for autor in autores[:3]:
            grupoA.agregar_equipo(autor)

        grupoB = Usuario("Grupo B")
        for autor in autores[3:]:
            grupoB.agregar_equipo(autor)

        self.biblioteca.registrar_grupo(grupoA)
        self.biblioteca.registrar_grupo(grupoB)

    def on_enter(self, e):
        e.widget['background'] = COLOR_MENU_CURSOR_ENCIMA

    def on_leave(self, e):
        e.widget['background'] = COLOR_MENU_LATERAL
    def config_window(self):
        # Configuración inicial de la ventana
        self.title('Python GUI')
        self.iconbitmap("imagenes/logo.ico")
        w, h = 1024, 600        
        util_ventana.centrar_ventana(self, w, h)        

    def paneles(self):        
        # Crear paneles: barra superior, menú lateral y cuerpo principal
        self.barra_superior = tk.Frame(self, bg=COLOR_BARRA_SUPERIOR, height=50)
        self.barra_superior.pack(side=tk.TOP, fill='both')      

        self.menu_lateral = tk.Frame(self, bg=COLOR_MENU_LATERAL, width=150)
        self.menu_lateral.pack(side=tk.LEFT, fill='both', expand=False) 
        
        self.cuerpo_principal = tk.Frame(self, bg=COLOR_CUERPO_PRINCIPAL)
        self.cuerpo_principal.pack(side=tk.RIGHT, fill='both', expand=True)
    
    def controles_barra_superior(self):
        # Configuración de la barra superior
        font_awesome = font.Font(family='FontAwesome', size=12)

        # Etiqueta de título
        self.labelTitulo = tk.Label(self.barra_superior, text="¡MENÚ MUNDIAL!")
        self.labelTitulo.config(fg="#fff", font=("Roboto", 15), bg=COLOR_BARRA_SUPERIOR, pady=10, width=16)
        self.labelTitulo.pack(side=tk.LEFT)

        # Botón del menú lateral
        self.buttonMenuLateral = tk.Button(self.barra_superior, text="\uf0c9", font=font_awesome,
                                           command=self.toggle_panel, bd=0, bg=COLOR_BARRA_SUPERIOR, fg="white")
        self.buttonMenuLateral.pack(side=tk.LEFT)

        # Etiqueta de informacion
        self.labelTitulo = tk.Label(self.barra_superior, text="POOUP@unipamplona.co")
        self.labelTitulo.config(fg="#fff", font=("Roboto", 10), bg=COLOR_BARRA_SUPERIOR, padx=10, width=20)
        self.labelTitulo.pack(side=tk.RIGHT)
    
    def toggle_panel(self):
        # Alternar la visibilidad del menú lateral
        if self.menu_lateral.winfo_viewable():
            self.menu_lateral.pack_forget()
        else:
            self.menu_lateral.pack(side=tk.LEFT, fill='both', expand=False)

    def controles_menu_lateral(self):
        # Configuración del menú lateral
        ancho_menu = 20
        alto_menu = 2
        self.menuLateralBtns = []

        botones_info = [
            ("Inicio", self.mostrar_inicio),
            ("Jugadores", self.mostrar_categorias),
            ("Equipos", self.mostrar_autores),
            ("Fixture", self.mostrar_fixture),
            ("Registrar un Equipo", self.registrar_equipo),
            ("Registrar un Jugador", self.registrar_jugador),
            ("Salir", self.destroy)
        ]

        for (text, command) in botones_info:
            btn = tk.Button(self.menu_lateral, text=text, bg=COLOR_MENU_LATERAL, fg="white", 
                            font=("Roboto", 13, "bold"), bd=0, padx=10, pady=10, width=ancho_menu, height=alto_menu,
                            command=command)
            btn.bind("<Enter>", self.on_enter)
            btn.bind("<Leave>", self.on_leave)
            btn.pack()
            self.menuLateralBtns.append(btn)

    def controles_cuerpo(self):
        # Controles del cuerpo principal
        self.cuerpo_label = tk.Label(self.cuerpo_principal, image=self.logo, bg=COLOR_CUERPO_PRINCIPAL)
        self.cuerpo_label.place(relx=0.5, rely=0.5, anchor='center')

    def mostrar_inicio(self):
        self.limpiar_cuerpo()
        self.cuerpo_label = tk.Label(self.cuerpo_principal, image=self.logo, bg=COLOR_CUERPO_PRINCIPAL)
        self.cuerpo_label.place(relx=0.5, rely=0.5, anchor='center')

    def limpiar_cuerpo(self):
        for widget in self.cuerpo_principal.winfo_children():
            widget.destroy()

    def mostrar_categorias(self):
        self.limpiar_cuerpo()
        info_categorias = self.biblioteca.mostrar_categorias()  # Mostrar categorías (jugadores)
        self.cuerpo_label = tk.Label(self.cuerpo_principal, text=info_categorias, bg=COLOR_CUERPO_PRINCIPAL, justify="left", font=("Roboto", 16))
        self.cuerpo_label.pack(padx=10, pady=10)


    def mostrar_fixture(self):
        self.limpiar_cuerpo()
        fixture = self.biblioteca.generar_fixture()
        self.cuerpo_label = tk.Label(self.cuerpo_principal, text=fixture, bg=COLOR_CUERPO_PRINCIPAL, justify="left", font=("Roboto", 16))
        self.cuerpo_label.pack(padx=10, pady=10)
        
    def mostrar_autores(self):
        self.limpiar_cuerpo()
        info_autores = self.biblioteca.mostrar_autores()  # Mostrar equipos (autores)
        self.cuerpo_label = tk.Label(self.cuerpo_principal, text=info_autores, bg=COLOR_CUERPO_PRINCIPAL, justify="left", font=("Roboto", 16))
        self.cuerpo_label.pack(padx=10, pady=10)

    def actualizar_lista_equipos(self):
        self.limpiar_cuerpo()
        info_equipos = self.biblioteca.mostrar_equipos()  # Obtener la lista actualizada de equipos
        self.cuerpo_label = tk.Label(self.cuerpo_principal, text=info_equipos, bg=COLOR_CUERPO_PRINCIPAL, justify="left", font=("Roboto", 16))
        self.cuerpo_label.pack(padx=10, pady=10)

    def registrar_equipo(self):
        self.limpiar_cuerpo()

        tk.Label(self.cuerpo_principal, text="Nombre del equipo:", bg=COLOR_CUERPO_PRINCIPAL,
                font=("Roboto", 14)).pack(pady=(10, 5))
        nombre_entry = tk.Entry(self.cuerpo_principal, width=50, font=("Roboto", 12))
        nombre_entry.pack()

        tk.Label(self.cuerpo_principal, text="País del equipo:", bg=COLOR_CUERPO_PRINCIPAL,
                font=("Roboto", 14)).pack(pady=(10, 5))
        pais_entry = tk.Entry(self.cuerpo_principal, width=50, font=("Roboto", 12))
        pais_entry.pack()

        tk.Label(self.cuerpo_principal, text="Año de fundación:", bg=COLOR_CUERPO_PRINCIPAL,
                font=("Roboto", 14)).pack(pady=(10, 5))
        fundacion_entry = tk.Entry(self.cuerpo_principal, width=50, font=("Roboto", 12))
        fundacion_entry.pack()

        def submit():
            nombre = nombre_entry.get()
            pais = pais_entry.get()
            fundacion = fundacion_entry.get()

            nuevo_equipo = Usuario(nombre, pais, fundacion)
            self.biblioteca.registrar_equipo(nuevo_equipo)
            messagebox.showinfo("Éxito", "Equipo registrado con éxito")
            self.actualizar_lista_equipos()  # Actualizar la lista de equipos en el menú lateral

        tk.Button(self.cuerpo_principal, text="Registrar", command=submit, width=20, font=("Roboto", 12)).pack(pady=10)

    def registrar_jugador(self):
        self.limpiar_cuerpo()

        tk.Label(self.cuerpo_principal, text="Nombre del jugador:", bg=COLOR_CUERPO_PRINCIPAL,
                font=("Roboto", 14)).pack(pady=(10, 5))
        nombre_entry = tk.Entry(self.cuerpo_principal, width=50, font=("Roboto", 12))
        nombre_entry.pack()

        tk.Label(self.cuerpo_principal, text="Edad del jugador:", bg=COLOR_CUERPO_PRINCIPAL,
                font=("Roboto", 14)).pack(pady=(10, 5))
        edad_entry = tk.Entry(self.cuerpo_principal, width=50, font=("Roboto", 12))
        edad_entry.pack()

        tk.Label(self.cuerpo_principal, text="Posición del jugador:", bg=COLOR_CUERPO_PRINCIPAL,
                font=("Roboto", 14)).pack(pady=(10, 5))
        posicion_entry = tk.Entry(self.cuerpo_principal, width=50, font=("Roboto", 12))
        posicion_entry.pack()

        def submit():
            nombre = nombre_entry.get()
            edad = edad_entry.get()
            posicion = posicion_entry.get()

            nuevo_jugador = Categoria(nombre, edad, posicion)
            self.biblioteca.registrar_categoria(nuevo_jugador)
            messagebox.showinfo("Éxito", "Jugador registrado con éxito")
            self.mostrar_categorias()

        tk.Button(self.cuerpo_principal, text="Registrar", command=submit, width=20, font=("Roboto", 12)).pack(pady=10)










