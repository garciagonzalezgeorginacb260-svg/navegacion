import tkinter as tk
from PIL import Image, ImageTk

# --- VENTANA ---
ventana = tk.Tk()
ventana.title("Fresita MKP")
ventana.geometry("800x600")
ventana.config(bg="white")

# --- COLORES ---
rosa_fuerte = "#f06f9b"
rosa_menu = "#f3c0d0"
blanco = "white"


# -----------------------------
#    PANTALLA DE LOGIN
# -----------------------------
def mostrar_login():
    for w in ventana.winfo_children():
        w.destroy()

    login_frame = tk.Frame(ventana, bg="white")
    login_frame.pack(expand=True)

    tk.Label(login_frame, text="Iniciar sesión", fg="black",
             bg="white", font=("Arial", 18, "bold")).pack(pady=10)

    tk.Label(login_frame, text="Usuario:", bg="white", fg="black").pack()
    usuario_entry = tk.Entry(login_frame)
    usuario_entry.pack(pady=5)

    tk.Label(login_frame, text="Contraseña:", bg="white", fg="black").pack()
    contrasena_entry = tk.Entry(login_frame, show="*")
    contrasena_entry.pack(pady=5)

    error_label = tk.Label(login_frame, text="", fg="red", bg="white")
    error_label.pack(pady=5)

    def validar_login():
        if usuario_entry.get() == "admin":
            if contrasena_entry.get() == "1234":
                construir_interfaz()
            else:
                error_label.config(text="Contraseña incorrecta")
        else:
            error_label.config(text="Usuario incorrecto")

    tk.Button(login_frame, text="Entrar",
              bg=rosa_fuerte, fg="white",
              command=validar_login).pack(pady=10)


# -----------------------------
#       INTERFAZ PRINCIPAL
# -----------------------------
def construir_interfaz():
    for w in ventana.winfo_children():
        w.destroy()

    global menu, contenido

    # MENÚ
    menu = tk.Frame(ventana, bg=rosa_menu, width=160)
    menu.pack(side="left", fill="y")

    # HEADER
    header = tk.Frame(ventana, bg=rosa_fuerte)
    header.pack(side="top", fill="x")

    def toggle_menu():
        if menu.winfo_viewable():
            menu.pack_forget()
        else:
            menu.pack(side="left", fill="y")

    tk.Button(header, text="☰", bg=rosa_fuerte, fg="white",
              font=("Arial", 20), bd=0,
              command=toggle_menu).pack(side="right", padx=10)

    # HEADER CONTENIDO
    header_contenido = tk.Frame(header, bg=rosa_fuerte)
    header_contenido.pack(side="left", pady=5)

    logo_img = None
    try:
        im = Image.open("logofresa.jpg").resize((45, 45))
        logo_img = ImageTk.PhotoImage(im)
    except:
        pass

    tk.Label(header_contenido, image=logo_img,
             bg=rosa_fuerte).grid(row=0, column=0, rowspan=2, padx=10)

    tk.Label(header_contenido, text="Fresita MKP", bg=rosa_fuerte, fg="white",
             font=("Arial", 18, "bold")).grid(row=0, column=1, sticky="w")

    tk.Label(header_contenido, text="belleza dulce como una fresa 🍓",
             bg=rosa_fuerte, fg="white").grid(row=1, column=1, sticky="w")

    # CONTENIDO
    contenido = tk.Frame(ventana, bg="white")
    contenido.pack(side="left", fill="both", expand=True)

    # FOOTER
    footer = tk.Frame(ventana, bg=rosa_fuerte)
    footer.pack(side="bottom", fill="x")
    tk.Label(footer, text="© 2025 Fresita MKP", bg=rosa_fuerte,
             fg=blanco).pack(fill="x")

    # -----------------------------
    #    FUNCIONES DE PANTALLAS
    # -----------------------------
    def limpiar():
        for w in contenido.winfo_children():
            w.destroy()

    # --- INICIO ---
    def mostrar_inicio():
        limpiar()
        tk.Label(contenido, text="Bienvenida a Fresita MKP",
                 font=("Arial", 18, "bold"),
                 bg=blanco).pack(pady=10)
        tk.Label(contenido, text="Tu sistema administrativo de maquillaje 🍓",
                 font=("Arial", 13),
                 bg=blanco).pack()

    # --- CONTACTO ---
    def mostrar_contacto():
        limpiar()
        tk.Label(contenido, text="Contacto", font=("Arial", 18, "bold"),
                 bg=blanco).pack(pady=10)

        tk.Label(contenido, text="Nombre:", bg=blanco).pack(anchor="w", padx=20)
        tk.Entry(contenido, width=40).pack(padx=20)

        tk.Label(contenido, text="Correo:", bg=blanco).pack(anchor="w", padx=20)
        tk.Entry(contenido, width=40).pack(padx=20)

        tk.Label(contenido, text="Comentario:", bg=blanco).pack(anchor="w", padx=20)
        tk.Text(contenido, width=45, height=5).pack(padx=20)

        tk.Button(contenido, text="Enviar", bg=rosa_fuerte,
                  fg="white").pack(pady=10)

        tk.Label(contenido, text="Soporte técnico:", font=("Arial", 12, "bold"),
                 bg=blanco).pack(anchor="w", padx=20, pady=10)
        tk.Label(contenido, text="Correo: soporte@fresitamkp.com", bg=blanco).pack(anchor="w", padx=40)
        tk.Label(contenido, text="Teléfono: 2212786000", bg=blanco).pack(anchor="w", padx=40)
        tk.Label(contenido, text="Horario: L-V, 9am a 6pm", bg=blanco).pack(anchor="w", padx=40)

    # --- INVENTARIO ---
    def mostrar_inventario():
        limpiar()
        tk.Label(contenido, text="Inventario", font=("Arial", 18, "bold"),
                 bg=blanco).pack(pady=10)

        productos = ["Rímel Prosa", "Rubor Pink Up", "Sombras Saniye", "Lip Oil Bissú"]

        for p in productos:
            tk.Label(contenido, text=f"- {p}", bg=blanco).pack(anchor="w", padx=20)

    # --- VENTAS ---
    def mostrar_ventas():
        limpiar()
        tk.Label(contenido, text="Ventas", font=("Arial", 18, "bold"),
                 bg=blanco).pack(pady=10)

        tk.Label(contenido, text="Producto vendido:", bg=blanco).pack(anchor="w", padx=20)
        tk.Entry(contenido, width=40).pack(padx=20)

        tk.Label(contenido, text="Monto:", bg=blanco).pack(anchor="w", padx=20)
        tk.Entry(contenido, width=40).pack(padx=20)

        tk.Button(contenido, text="Registrar venta", bg=rosa_fuerte,
                  fg="white").pack(pady=10)

    # --- CLIENTES ---
    def mostrar_clientes():
        limpiar()
        tk.Label(contenido, text="Clientes", font=("Arial", 18, "bold"),
                 bg=blanco).pack(pady=10)

        tk.Label(contenido, text="Nombre del cliente:", bg=blanco).pack(anchor="w", padx=20)
        tk.Entry(contenido).pack(padx=20)
        tk.Button(contenido, text="Guardar", bg=rosa_fuerte, fg="white").pack(pady=5)

    # --- PRODUCTOS ---
    def mostrar_productos():
        limpiar()
        tk.Label(contenido, text="Catálogo de Productos",
                 font=("Arial", 18, "bold"), bg=blanco).pack(pady=10)

        lista = ["Labial", "Rímel", "Rubor", "Sombras"]
        for p in lista:
            tk.Label(contenido, text=f"• {p}", bg=blanco).pack(anchor="w", padx=20)

    # --- PEDIDOS ---
    def mostrar_pedidos():
        limpiar()
        tk.Label(contenido, text="Pedidos", font=("Arial", 18, "bold"),
                 bg=blanco).pack(pady=10)

        tk.Label(contenido, text="Cliente:", bg=blanco).pack(anchor="w", padx=20)
        tk.Entry(contenido).pack(padx=20)

        tk.Label(contenido, text="Producto:", bg=blanco).pack(anchor="w", padx=20)
        tk.Entry(contenido).pack(padx=20)

        tk.Button(contenido, text="Guardar pedido", bg=rosa_fuerte,
                  fg="white").pack(pady=10)

    # --- REPORTES ---
    def mostrar_reportes():
        limpiar()
        tk.Label(contenido, text="Reportes", font=("Arial", 18, "bold"),
                 bg=blanco).pack(pady=10)

        tk.Label(contenido, text="• Reporte semanal: $1500 MXN", bg=blanco).pack(anchor="w", padx=20)
        tk.Label(contenido, text="• Reporte mensual: $6200 MXN", bg=blanco).pack(anchor="w", padx=20)

    # --- ACERCA DE ---
    def mostrar_acerca():
        limpiar()
        tk.Label(contenido, text="Acerca de Fresita MKP",
                 font=("Arial", 18, "bold"), bg=blanco).pack(pady=10)

        tk.Label(contenido,
                 text="Emprendimiento de maquillaje\ncreado con amor y estilo en México 🍓",
                 bg=blanco, font=("Arial", 12)).pack()

    # --- AJUSTES ---
    def mostrar_ajustes():
        limpiar()
        tk.Label(contenido, text="Ajustes", font=("Arial", 18, "bold"),
                 bg=blanco).pack(pady=10)

        tk.Label(contenido, text="Cambiar usuario/contraseña próximamente...",
                 bg=blanco).pack()

    # -----------------------------
    # BOTONES DEL MENÚ
    # -----------------------------
    opciones = [
        ("Inicio", mostrar_inicio),
        ("Contacto", mostrar_contacto),
        ("Inventario", mostrar_inventario),
        ("Ventas", mostrar_ventas),
        ("Clientes", mostrar_clientes),
        ("Productos", mostrar_productos),
        ("Pedidos", mostrar_pedidos),
        ("Reportes", mostrar_reportes),
        ("Acerca de", mostrar_acerca),
        ("Ajustes", mostrar_ajustes)
    ]

    for texto, comando in opciones:
        tk.Button(menu, text=texto, bg=rosa_menu, fg="black",
                  relief="flat", command=comando).pack(fill="x", pady=2)

    mostrar_inicio()


# EJECUTAR LOGIN PRIMERO
mostrar_login()
ventana.mainloop()
