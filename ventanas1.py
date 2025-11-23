import tkinter as tk

# --- VENTANA PRINCIPAL ---
ventana = tk.Tk()
ventana.title("Fresita MKP")
ventana.geometry("600x500")
ventana.config(bg="white")

# --- COLORES ---
rosa_fuerte = "#f06f9b"  # rosa fuerte para header y footer
blanco = "white"
rosa_menu = "#f3c0d0"    # rosa suave para menú lateral

# --- HEADER ---
header = tk.Frame(ventana, bg=blanco)
header.pack(side="top", fill="x")

tk.Label(header, text="Fresita MKP", bg=rosa_fuerte, fg=blanco, font=("Arial", 18, "bold")).pack(pady=5, fill="x")
tk.Label(header, text="belleza dulce como una fresa 🍓", bg=rosa_fuerte, fg=blanco, font=("Arial", 10)).pack(fill="x")

# --- MENÚ LATERAL ---
menu = tk.Frame(ventana, bg=rosa_menu, width=150)
menu.pack(side="left", fill="y")

# --- CONTENIDO PRINCIPAL ---
contenido = tk.Frame(ventana, bg=blanco)
contenido.pack(side="left", fill="both", expand=True)

# --- FOOTER ---
footer = tk.Frame(ventana, bg=blanco)
footer.pack(side="bottom", fill="x")

tk.Label(footer, text="© 2025 Fresita MKP", bg=rosa_fuerte, fg=blanco, font=("Arial", 9)).pack(fill="x")
tk.Label(footer, text="📸  💄  💋  🍓", bg=rosa_fuerte, fg=blanco, font=("Arial", 12)).pack(fill="x", pady=2)

# --- FUNCIONES ---
def limpiar_contenido():
    for w in contenido.winfo_children():
        w.destroy()

# ---- INICIO / MISION Y VISION ----
def mostrar_inicio():
    limpiar_contenido()
    tk.Label(contenido, text="Bienvenido a Fresita MKP", bg=blanco, fg="black", font=("Arial", 16, "bold")).pack(pady=10)
    
    tk.Label(contenido, text="Misión:", bg=blanco, fg="black", font=("Arial", 12, "bold")).pack(anchor="w", padx=20, pady=5)
    tk.Label(contenido, text="Ofrecer productos de belleza de calidad que resalten la dulzura y estilo de nuestras clientas.", bg=blanco).pack(anchor="w", padx=40)
    
    tk.Label(contenido, text="Visión:", bg=blanco, fg="black", font=("Arial", 12, "bold")).pack(anchor="w", padx=20, pady=5)
    tk.Label(contenido, text="Ser la marca de referencia en belleza dulce y creativa, destacando por un servicio cercano y personalizado.", bg=blanco).pack(anchor="w", padx=40)

# ---- PRODUCTOS ----
def mostrar_productos():
    limpiar_contenido()
    tk.Label(contenido, text="Lista de productos", bg=blanco, fg="black", font=("Arial", 14, "bold")).pack(pady=5, anchor="w", padx=20)

    productos = [
        ("Rubor", 60, 5),
        ("Rímel Prosa", 45, 8),
        ("Sombras Saniye", 40, 6),
        ("Lip Oil Pink Up", 80, 4),
        ("Rubor Bissú", 60, 7)
    ]

    for nombre, precio, cantidad in productos:
        tk.Label(contenido, text=f"{nombre} - ${precio}  Cantidad: {cantidad}", bg=blanco, font=("Arial", 10)).pack(anchor="w", padx=40)

    tk.Button(contenido, text="+ Agregar más", bg=rosa_menu, fg=blanco, relief="flat").pack(pady=10, anchor="w", padx=20)

    tk.Label(contenido, text="Poco inventario", bg=blanco, fg="black", font=("Arial", 12, "bold")).pack(pady=5, anchor="w", padx=20)
    pocos = [
        ("Pestañas", 55, 4),
        ("Aceite Prosa", 60, 3)
    ]
    for nombre, precio, cantidad in pocos:
        tk.Label(contenido, text=f"{nombre} - ${precio}  Cantidad: {cantidad}", bg=blanco, font=("Arial", 10)).pack(anchor="w", padx=40)

# ---- PEDIDOS ----
def mostrar_pedidos():
    limpiar_contenido()
    tk.Label(contenido, text="Lista de pedidos", bg=blanco, fg="black", font=("Arial", 14, "bold")).pack(pady=5, anchor="w", padx=20)
    
    # Botón para agregar nuevo pedido
    tk.Button(contenido, text="+ Agregar nuevo pedido", bg=rosa_menu, fg=blanco).pack(anchor="w", padx=20, pady=5)

    # Pendientes
    tk.Label(contenido, text="Pendientes", bg=blanco, fg="black", font=("Arial", 12, "bold")).pack(anchor="w", padx=40, pady=5)
    pendientes = [
        ("Pedido 1", "Fulanita", "Rímel", 48),
        ("Pedido 2", "Mariana", "Rubor", 60)
    ]
    for num, cliente, producto, total in pendientes:
        tk.Label(contenido, text=f"{num}: Cliente: {cliente} | Producto: {producto} | Total: ${total}", bg=blanco, font=("Arial", 10)).pack(anchor="w", padx=60)

    # Entregados
    tk.Label(contenido, text="Entregados", bg=blanco, fg="black", font=("Arial", 12, "bold")).pack(anchor="w", padx=40, pady=10)
    entregados = [
        ("Pedido 3", "Andrea", "Lip Oil", 80),
        ("Pedido 4", "Sofía", "Sombras", 40),
        ("Pedido 5", "Luz", "Rubor Bissú", 60)
    ]
    for num, cliente, producto, total in entregados:
        tk.Label(contenido, text=f"{num}: Cliente: {cliente} | Producto: {producto} | Total: ${total}", bg=blanco, font=("Arial", 10)).pack(anchor="w", padx=60)

# ---- CONFIGURACIÓN ----
def mostrar_configuracion():
    limpiar_contenido()
    tk.Label(contenido, text="Configuración", bg=blanco, fg="black", font=("Arial", 14, "bold")).pack(pady=5, anchor="w", padx=20)
    
    def toggle(frame, button):
        if frame.winfo_viewable():
            frame.pack_forget()
            button.config(text=button.cget("text").replace("▼", "▸"))
        else:
            frame.pack(anchor="w", padx=40)
            button.config(text=button.cget("text").replace("▸", "▼"))
    
    # PERFIL DE NEGOCIO
    perfil_frame = tk.Frame(contenido, bg=blanco)
    perfil_button = tk.Button(contenido, text="Perfil de negocio ▸", bg=rosa_menu, fg=blanco, relief="flat",
                             command=lambda: toggle(perfil_frame, perfil_button))
    perfil_button.pack(anchor="w", padx=20, pady=2)
    tk.Label(perfil_frame, text="- Nombre", bg=blanco).pack(anchor="w")
    tk.Label(perfil_frame, text="- Descripción", bg=blanco).pack(anchor="w")
    tk.Label(perfil_frame, text="- Misión y visión", bg=blanco).pack(anchor="w")

    # MÉTODOS DE PAGO
    pagos_frame = tk.Frame(contenido, bg=blanco)
    pagos_button = tk.Button(contenido, text="Métodos de pago ▸", bg=rosa_menu, fg=blanco, relief="flat",
                             command=lambda: toggle(pagos_frame, pagos_button))
    pagos_button.pack(anchor="w", padx=20, pady=2)
    tk.Label(pagos_frame, text="- Efectivo", bg=blanco).pack(anchor="w")
    tk.Label(pagos_frame, text="- Tarjeta", bg=blanco).pack(anchor="w")
    tk.Label(pagos_frame, text="- Transferencia bancaria", bg=blanco).pack(anchor="w")

    # PREFERENCIAS
    pref_frame = tk.Frame(contenido, bg=blanco)
    pref_button = tk.Button(contenido, text="Preferencias ▸", bg=rosa_menu, fg=blanco, relief="flat",
                            command=lambda: toggle(pref_frame, pref_button))
    pref_button.pack(anchor="w", padx=20, pady=2)
    tk.Label(pref_frame, text="- Notificaciones", bg=blanco).pack(anchor="w")
    tk.Label(pref_frame, text="- Tema de la página", bg=blanco).pack(anchor="w")
    tk.Label(pref_frame, text="- Idioma", bg=blanco).pack(anchor="w")
    tk.Label(pref_frame, text="- Moneda", bg=blanco).pack(anchor="w")

    # SEGURIDAD
    seg_frame = tk.Frame(contenido, bg=blanco)
    seg_button = tk.Button(contenido, text="Seguridad ▸", bg=rosa_menu, fg=blanco, relief="flat",
                           command=lambda: toggle(seg_frame, seg_button))
    seg_button.pack(anchor="w", padx=20, pady=2)
    tk.Label(seg_frame, text="- Contraseña", bg=blanco).pack(anchor="w")
    tk.Label(seg_frame, text="- Copia de respaldo", bg=blanco).pack(anchor="w")
    tk.Label(seg_frame, text="- Cerrar sesión", bg=blanco).pack(anchor="w")
   
    # ---- CLIENTES CON TABLA ----
def mostrar_clientes():
    limpiar_contenido()
    tk.Label(contenido, text="Clientes", bg=blanco, fg="black", font=("Arial", 14, "bold")).pack(pady=5, anchor="w", padx=20)

    clientes = [
        ("Carlita", "555-1234", "Rubor Bissú", "Entrega rápida"),
        ("Mariana", "555-5678", "Rímel Prosa", "Pide sombras la próxima"),
        ("Andrea", "555-8765", "Lip Oil", "Cliente frecuente")
    ]

    tabla = tk.Frame(contenido, bg=blanco)
    tabla.pack(padx=20, pady=10, anchor="w")

    encabezado = ["Nombre", "Contacto", "Última compra", "Nota rápida"]
    for i, titulo in enumerate(encabezado):
        tk.Label(tabla, text=titulo, bg=rosa_menu, fg=blanco, font=("Arial", 10, "bold"), width=18, borderwidth=1, relief="solid").grid(row=0, column=i)

    for fila_num, fila_datos in enumerate(clientes, start=1):
        for col_num, dato in enumerate(fila_datos):
            tk.Label(tabla, text=dato, bg=blanco, font=("Arial", 10), width=18, borderwidth=1, relief="solid").grid(row=fila_num, column=col_num)

# ---- VENTAS COMPLETAS ----
def mostrar_ventas():
    limpiar_contenido()
    tk.Label(contenido, text="Ventas", bg=blanco, fg="black", font=("Arial", 14, "bold")).pack(pady=5, anchor="w", padx=20)

    # Resumen general
    tk.Label(contenido, text="Resumen general", bg=blanco, fg="black", font=("Arial", 12, "bold")).pack(anchor="w", padx=40, pady=5)
    tk.Label(contenido, text="Ventas del día: $500", bg=blanco).pack(anchor="w", padx=60)
    tk.Label(contenido, text="Ventas de la semana: $3200", bg=blanco).pack(anchor="w", padx=60)
    tk.Label(contenido, text="Ganancia: $1500", bg=blanco).pack(anchor="w", padx=60)
    tk.Label(contenido, text="Total pedidos: 45", bg=blanco).pack(anchor="w", padx=60)

    # Productos más vendidos
    tk.Label(contenido, text="Productos más vendidos", bg=blanco, fg="black", font=("Arial", 12, "bold")).pack(anchor="w", padx=40, pady=5)
    productos_mas_vendidos = ["Labial", "Rubor Bissú", "Rímel Prosa", "Sombras Saniye", "Lip Oil Pink Up"]
    for producto in productos_mas_vendidos:
        tk.Label(contenido, text=f"- {producto}", bg=blanco).pack(anchor="w", padx=60)

    # Ventas recientes (tabla)
    tk.Label(contenido, text="Ventas recientes", bg=blanco, fg="black", font=("Arial", 12, "bold")).pack(anchor="w", padx=40, pady=10)

    ventas = [
        ("29/10/2025", "Fulanita", "Rubor Bissú", "$60", "Efectivo"),
        ("28/10/2025", "Mariana", "Rímel Prosa", "$45", "Tarjeta"),
        ("27/10/2025", "Andrea", "Lip Oil", "$80", "Transferencia")
    ]
    
    tabla_ventas = tk.Frame(contenido, bg=blanco)
    tabla_ventas.pack(padx=20, pady=5, anchor="w")

    encabezado_ventas = ["Fecha", "Cliente", "Productos", "Total", "Método de pago"]
    for i, titulo in enumerate(encabezado_ventas):
        tk.Label(tabla_ventas, text=titulo, bg=rosa_menu, fg=blanco, font=("Arial", 10, "bold"), width=15, borderwidth=1, relief="solid").grid(row=0, column=i)

    for fila_num, fila_datos in enumerate(ventas, start=1):
        for col_num, dato in enumerate(fila_datos):
            tk.Label(tabla_ventas, text=dato, bg=blanco, font=("Arial", 10), width=15, borderwidth=1, relief="solid").grid(row=fila_num, column=col_num)

# --- BOTONES MENÚ ---
tk.Button(menu, text="Inicio", bg=rosa_menu, fg=blanco, relief="flat", command=mostrar_inicio).pack(fill="x", pady=2)
tk.Button(menu, text="Productos", bg=rosa_menu, fg=blanco, relief="flat", command=mostrar_productos).pack(fill="x", pady=2)
tk.Button(menu, text="Pedidos", bg=rosa_menu, fg=blanco, relief="flat", command=mostrar_pedidos).pack(fill="x", pady=2)
tk.Button(menu, text="Configuración", bg=rosa_menu, fg=blanco, relief="flat", command=mostrar_configuracion).pack(fill="x", pady=2)
tk.Button(menu, text="Clientes", bg=rosa_menu, fg=blanco, relief="flat", command=mostrar_clientes).pack(fill="x", pady=2)
tk.Button(menu, text="Ventas", bg=rosa_menu, fg=blanco, relief="flat", command=mostrar_ventas).pack(fill="x", pady=2)

# Mostrar inicio por defecto
mostrar_inicio()

ventana.mainloop()