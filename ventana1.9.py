import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# =====================================================
# ===================== LOGIN ==========================
# =====================================================

def login_screen():
    login = tk.Tk()
    login.title("Fresita MKP - Login Dueño")
    login.geometry("350x300")
    login.config(bg="white")

    tk.Label(login, text="Fresita MKP", font=("Arial", 20, "bold"), bg="white", fg="#f06f9b").pack(pady=10)
    tk.Label(login, text="Inicio de sesión del dueño", font=("Arial", 12), bg="white").pack()

    tk.Label(login, text="Usuario:", bg="white").pack(pady=5)
    user_entry = tk.Entry(login)
    user_entry.pack()

    tk.Label(login, text="Contraseña:", bg="white").pack(pady=5)
    pass_entry = tk.Entry(login, show="*")
    pass_entry.pack()

    def verificar():
        user = user_entry.get()
        pwd = pass_entry.get()

        if user == "dueño" and pwd == "1234":
            login.destroy()
            main_app()
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")

    tk.Button(login, text="Entrar", bg="#f06f9b", fg="white", command=verificar).pack(pady=15)

    login.mainloop()


# =====================================================
# ===================== APP PRINCIPAL ==================
# =====================================================

def main_app():
    ventana = tk.Tk()
    ventana.title("Fresita MKP")
    ventana.geometry("600x500")
    ventana.config(bg="white")

    rosa_fuerte = "#f06f9b"
    blanco = "white"
    rosa_menu = "#f3c0d0"

    # --- HEADER ---
    header = tk.Frame(ventana, bg=rosa_fuerte)
    header.pack(side="top", fill="x")

    def toggle_menu():
        if menu.winfo_viewable():
            menu.pack_forget()
        else:
            menu.pack(side="left", fill="y")

    btn_hamb = tk.Button(header, text="☰", font=("Arial", 20, "bold"),
                        bg=rosa_fuerte, fg="white", bd=0,
                        activebackground=rosa_fuerte, command=toggle_menu)
    btn_hamb.pack(side="right", padx=10)

    # Contenedor
    header_contenido = tk.Frame(header, bg=rosa_fuerte)
    header_contenido.pack(side="left", pady=5)

    # Logo
    logo_original = Image.open("logofresa.jpg")
    logo_original = logo_original.resize((45, 45))
    logo_img = ImageTk.PhotoImage(logo_original)

    tk.Label(header_contenido, image=logo_img, bg=rosa_fuerte).grid(row=0, column=0, rowspan=2, padx=10)

    tk.Label(header_contenido, text="Fresita MKP", fg="white",
             bg=rosa_fuerte, font=("Arial", 18, "bold")).grid(row=0, column=1, sticky="w")

    tk.Label(header_contenido, text="belleza dulce como una fresa 🍓",
             fg="white", bg=rosa_fuerte, font=("Arial", 10)).grid(row=1, column=1, sticky="w")

    # --- MENÚ ---
    menu = tk.Frame(ventana, bg=rosa_menu, width=150)
    menu.pack(side="left", fill="y")

    # --- CONTENIDO ---
    contenido = tk.Frame(ventana, bg=blanco)
    contenido.pack(side="left", fill="both", expand=True)

    # --- FOOTER ---
    footer = tk.Frame(ventana, bg=blanco)
    footer.pack(side="bottom", fill="x")
    tk.Label(footer, text="© 2025 Fresita MKP - Derechos reservados",
             bg=rosa_fuerte, fg="white").pack(fill="x")

    def limpiar():
        for w in contenido.winfo_children():
            w.destroy()

    # =====================================================
    # ===================== PANTALLAS ======================
    # =====================================================

    # ---- INICIO / MISIÓN / VISIÓN ----
    def mostrar_inicio():
        limpiar()
        tk.Label(contenido, text="Bienvenido a Fresita MKP",
                 font=("Arial", 18, "bold"), bg=blanco).pack(pady=10)

        intro = """Fresita MKP es un emprendimiento dedicado al maquillaje,
para chicas que aman verse dulces, bonitas y con mucho estilo."""

        tk.Label(contenido, text=intro, bg=blanco, font=("Arial", 11)).pack(pady=5)

        tk.Label(contenido, text="Misión", font=("Arial", 14, "bold"), bg=blanco).pack(pady=5)
        tk.Label(contenido, text="Ofrecer belleza accesible y dulce como una fresa.",
                 bg=blanco).pack()

        tk.Label(contenido, text="Visión", font=("Arial", 14, "bold"), bg=blanco).pack(pady=5)
        tk.Label(contenido, text="Ser la marca preferida de maquillaje juvenil en México.",
                 bg=blanco).pack()

    # ---- CONTACTO / SUGERENCIAS ----
    def mostrar_contacto():
        limpiar()
        tk.Label(contenido, text="Contacto de la Empresa",
                 font=("Arial", 16, "bold"), bg=blanco).pack(pady=10)

        datos = (
            "📍 Ubicación: Monterrey, Nuevo León\n"
            "📱 WhatsApp: 818-000-0000\n"
            "📸 Instagram: @fresitamkp\n"
            "💌 Correo: fresitamkp@gmail.com"
        )

        tk.Label(contenido, text=datos, bg=blanco, font=("Arial", 11), justify="left").pack(pady=5)

        tk.Label(contenido, text="Sugerencias", font=("Arial", 14, "bold"), bg=blanco).pack(pady=10)

        suger = tk.Text(contenido, height=5, width=40)
        suger.pack()

        def enviar_sugerencia():
            messagebox.showinfo("Gracias", "Tu sugerencia fue enviada ✔")

        tk.Button(contenido, text="Enviar", bg=rosa_fuerte, fg="white",
                  command=enviar_sugerencia).pack(pady=10)

    # ---- EDITAR PERFIL ----
    def mostrar_perfil():
        limpiar()
        tk.Label(contenido, text="Editar perfil del dueño",
                 font=("Arial", 16, "bold"), bg=blanco).pack(pady=10)

        tk.Label(contenido, text="(El nombre de usuario no se puede cambiar)",
                 bg=blanco, fg="gray").pack()

        tk.Label(contenido, text="Usuario: dueño", font=("Arial", 12, "bold"),
                 bg=blanco).pack(pady=10)

        tk.Label(contenido, text="Cambiar descripción del perfil:", bg=blanco).pack()
        caja_desc = tk.Entry(contenido, width=40)
        caja_desc.pack(pady=5)

        tk.Label(contenido, text="Cambiar foto de perfil (no funcional):", bg=blanco).pack(pady=5)

        tk.Button(contenido, text="Subir nueva foto",
                  bg=rosa_menu, fg="white").pack()

        tk.Button(contenido, text="Guardar cambios", bg=rosa_fuerte,
                  fg="white").pack(pady=15)

    # =====================================================
    # ================= BOTONES DEL MENÚ ==================
    # =====================================================

    tk.Button(menu, text="Inicio", bg=rosa_menu, fg="white", relief="flat",
              command=mostrar_inicio).pack(fill="x", pady=2)

    tk.Button(menu, text="Contacto", bg=rosa_menu, fg="white", relief="flat",
              command=mostrar_contacto).pack(fill="x", pady=2)

    tk.Button(menu, text="Editar Perfil", bg=rosa_menu, fg="white", relief="flat",
              command=mostrar_perfil).pack(fill="x", pady=2)

    # ---- Botones que ya tenías ----
    # puedes agregarlos aquí si quieres

    mostrar_inicio()
    ventana.mainloop()


# Iniciar la app con login
login_screen()
