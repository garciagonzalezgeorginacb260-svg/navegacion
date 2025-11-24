import tkinter as tk
from PIL import Image, ImageTk

# ---------------------------------------------------
#                FUNCIÓN PRINCIPAL
# ---------------------------------------------------
def iniciar_sistema():
    ventana = tk.Tk()
    ventana.title("Fresita MKP")
    ventana.geometry("600x500")
    ventana.config(bg="white")

    # --- COLORES ---
    rosa_fuerte = "#f06f9b"
    blanco = "white"
    rosa_menu = "#f3c0d0"

    # ---------------------------------------------------
    #                      HEADER
    # ---------------------------------------------------
    header = tk.Frame(ventana, bg=rosa_fuerte)
    header.pack(side="top", fill="x")

    # MENÚ DESPLEGABLE
    def toggle_menu():
        if menu.winfo_viewable():
            menu.pack_forget()
        else:
            menu.pack(side="left", fill="y")

    btn_hamb = tk.Button(header, text="☰", font=("Arial", 20, "bold"),
                         bg=rosa_fuerte, fg="white", bd=0,
                         command=toggle_menu)
    btn_hamb.pack(side="right", padx=10)

    # Contenedor interno (logo + texto)
    header_contenido = tk.Frame(header, bg=rosa_fuerte)
    header_contenido.pack(side="left", pady=5)

    # Logo
    try:
        logo_original = Image.open("logofresa.jpg")
        logo_original = logo_original.resize((45, 45))
        logo_img = ImageTk.PhotoImage(logo_original)
        label_logo = tk.Label(header_contenido, image=logo_img, bg=rosa_fuerte)
        label_logo.image = logo_img
        label_logo.grid(row=0, column=0, rowspan=2, padx=10)
    except:
        tk.Label(header_contenido, text="🍓", font=("Arial",30),
                 bg=rosa_fuerte, fg="white").grid(row=0,column=0,rowspan=2,padx=10)

    # Nombre
    tk.Label(header_contenido, text="Fresita MKP",
             bg=rosa_fuerte, fg="white",
             font=("Arial", 18, "bold")).grid(row=0, column=1, sticky="w")

    # Slogan
    tk.Label(header_contenido, text="belleza dulce como una fresa 🍓",
             bg=rosa_fuerte, fg="white",
             font=("Arial", 10)).grid(row=1, column=1, sticky="w")

    # ---------------------------------------------------
    #                     MENÚ LATERAL
    # ---------------------------------------------------
    menu = tk.Frame(ventana, bg=rosa_menu, width=150)
    menu.pack(side="left", fill="y")

    # ---------------------------------------------------
    #                     CONTENIDO
    # ---------------------------------------------------
    contenido = tk.Frame(ventana, bg=blanco)
    contenido.pack(side="left", fill="both", expand=True)

    def limpiar():
        for w in contenido.winfo_children():
            w.destroy()

    # ---------------------------------------------------
    #                  PANTALLAS DEL SISTEMA
    # ---------------------------------------------------

    # ---------- INICIO ----------
    def inicio():
        limpiar()
        tk.Label(contenido, text="Bienvenida a Fresita MKP",
                 bg=blanco, fg="black", font=("Arial",16,"bold")).pack(pady=10)

    # ---------- PRODUCTOS ----------
    def productos():
        limpiar()
        tk.Label(contenido, text="Productos", bg=blanco,
                 font=("Arial", 16, "bold")).pack(pady=10)

    # ---------- PEDIDOS ----------
    def pedidos():
        limpiar()
        tk.Label(contenido, text="Pedidos", bg=blanco,
                 font=("Arial", 16, "bold")).pack(pady=10)

    # ---------- CONFIGURACIÓN ----------
    def configuracion():
        limpiar()
        tk.Label(contenido, text="Configuración", bg=blanco,
                 font=("Arial", 16, "bold")).pack(pady=10)

    # ---------- CLIENTES ----------
    def clientes():
        limpiar()
        tk.Label(contenido, text="Clientes", bg=blanco,
                 font=("Arial", 16, "bold")).pack(pady=10)

    # ---------- VENTAS ----------
    def ventas():
        limpiar()
        tk.Label(contenido, text="Ventas", bg=blanco,
                 font=("Arial", 16, "bold")).pack(pady=10)

    # ---------- CONTACTO ----------
    def contacto():
        limpiar()

        tk.Label(contenido, text="Contacto", bg=blanco,
                 font=("Arial", 16, "bold")).pack(pady=10)

        tk.Label(contenido, text="Nombre de usuario:", bg=blanco).pack(anchor="w", padx=20)
        entrada_user = tk.Entry(contenido, width=40)
        entrada_user.pack(anchor="w", padx=20, pady=3)

        tk.Label(contenido, text="Correo:", bg=blanco).pack(anchor="w", padx=20)
        entrada_correo = tk.Entry(contenido, width=40)
        entrada_correo.pack(anchor="w", padx=20, pady=3)

        tk.Label(contenido, text="Comentario:", bg=blanco).pack(anchor="w", padx=20)
        entrada_coment = tk.Text(contenido, width=45, height=5)
        entrada_coment.pack(anchor="w", padx=20, pady=3)

        tk.Button(contenido, text="Enviar", bg=rosa_menu, fg=blanco, width=12).pack(padx=20, pady=10)

        # --- Soporte técnico ---
        tk.Label(contenido, text="Datos de soporte técnico", bg=blanco,
                 font=("Arial", 12, "bold")).pack(pady=10)

        tk.Label(contenido, text="Correo: soporte@fresitamkp.com", bg=blanco).pack()
        tk.Label(contenido, text="Teléfono: 2212786000", bg=blanco).pack()
        tk.Label(contenido, text="Horario: lunes a viernes 9:00 a 18:00", bg=blanco).pack()

    # ---------------------------------------------------
    #               BOTONES DEL MENÚ
    # ---------------------------------------------------
    tk.Button(menu, text="Inicio", bg=rosa_menu, fg=blanco, relief="flat",
              command=inicio).pack(fill="x", pady=2)
    tk.Button(menu, text="Productos", bg=rosa_menu, fg=blanco, relief="flat",
              command=productos).pack(fill="x", pady=2)
    tk.Button(menu, text="Pedidos", bg=rosa_menu, fg=blanco, relief="flat",
              command=pedidos).pack(fill="x", pady=2)
    tk.Button(menu, text="Configuración", bg=rosa_menu, fg=blanco, relief="flat",
              command=configuracion).pack(fill="x", pady=2)
    tk.Button(menu, text="Clientes", bg=rosa_menu, fg=blanco, relief="flat",
              command=clientes).pack(fill="x", pady=2)
    tk.Button(menu, text="Ventas", bg=rosa_menu, fg=blanco, relief="flat",
              command=ventas).pack(fill="x", pady=2)
    tk.Button(menu, text="Contacto", bg=rosa_menu, fg=blanco, relief="flat",
              command=contacto).pack(fill="x", pady=2)

    # INICIO POR DEFECTO
    inicio()

    ventana.mainloop()

# ---------------------------------------------------
#              PANTALLA DE LOGIN
# ---------------------------------------------------
def login_screen():
    login = tk.Tk()
    login.title("Login Fresita MKP")
    login.geometry("300x250")
    login.config(bg="white")

    tk.Label(login, text="Iniciar sesión", font=("Arial",16,"bold"),
             bg="white").pack(pady=10)

    tk.Label(login, text="Usuario:", bg="white").pack()
    user_entry = tk.Entry(login)
    user_entry.pack()

    tk.Label(login, text="Contraseña:", bg="white").pack()
    pass_entry = tk.Entry(login, show="*")
    pass_entry.pack()

    def validar():
        if user_entry.get() == "admin" and pass_entry.get() == "1234":
            login.destroy()
            iniciar_sistema()
        else:
            tk.Label(login, text="Datos incorrectos", fg="red", bg="white").pack()

    tk.Button(login, text="Entrar", bg="#f3c0d0",
              command=validar).pack(pady=10)

    login.mainloop()

# Iniciar programa
login_screen()
