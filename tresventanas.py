import tkinter as tk
from tkinter import ttk

def regresar(ventana_origen, ventana_actual):
    ventana_actual.destroy()
    ventana_origen.deiconify()

def mostrar_ventana(origen, destino_func):
    origen.withdraw()
    destino_func(origen)


def ventana_informacion(ventana1):
    v = tk.Toplevel(ventana1)
    v.title("Información de FresitaMKP")
    v.geometry("600x350")

    ttk.Label(v, text="Misión de FresitaMKP:\nBrindar productos accesibles y de calidad.").pack(pady=5)
    ttk.Label(v, text="Visión de FresitaMKP:\nSer un emprendimiento reconocido en belleza.").pack(pady=5)
    ttk.Label(v, text="Datos de la Empresa:\nCorreo: contacto@fresitamkp.com\nTeléfono: +52 55 1234 5678\nCódigo Postal: 12345").pack(pady=5)

    ttk.Button(v, text="Regresar al Inicio",
               command=lambda: regresar(ventana1, v)).pack(pady=15)


def ventana_contacto(ventana1):
    v = tk.Toplevel(ventana1)
    v.title("Formulario de Contacto - FresitaMKP")
    v.geometry("500x600")

    ttk.Label(v, text="Nombre del usuario:").pack(pady=5, anchor='w')
    ttk.Entry(v, width=40).pack(pady=5)

    ttk.Label(v, text="Correo:").pack(pady=5, anchor='w')
    ttk.Entry(v, width=40).pack(pady=5)

    ttk.Label(v, text="Comentario a enviar:").pack(pady=5, anchor='w')
    tk.Text(v, height=5, width=40).pack(pady=5)

    ttk.Button(v, text="Aceptar").pack(pady=10)
    ttk.Label(v, text="Datos de Soporte Técnico:\nCorreo: soporte@fresitamkp.com\nTeléfono: +52 55 9876 5432\nHorario: Lunes a Viernes, 9:00 a 18:00").pack(pady=10)

    ttk.Button(v, text="Regresar al Inicio",
               command=lambda: regresar(ventana1, v)).pack(pady=15)


def main():
    ventana1 = tk.Tk()
    ventana1.title("Inicio de Sesión - FresitaMKP")
    ventana1.geometry("500x400")

    ttk.Label(ventana1, text="Usuario:").pack(pady=5)
    ttk.Entry(ventana1).pack()

    ttk.Label(ventana1, text="Contraseña:").pack(pady=5)
    ttk.Entry(ventana1, show="*").pack()

    ttk.Button(ventana1, text="Iniciar Sesión").pack(pady=10)
    ttk.Button(ventana1, text="Iniciar con Facebook").pack(pady=5)
    ttk.Button(ventana1, text="Iniciar con Google").pack(pady=5)

    ttk.Button(
        ventana1, text="Ver Información de la Empresa",
        command=lambda: mostrar_ventana(ventana1, ventana_informacion)
    ).pack(pady=10)

    ttk.Button(
        ventana1, text="Ir al Formulario de Contacto",
        command=lambda: mostrar_ventana(ventana1, ventana_contacto)
    ).pack(pady=10)

    ventana1.mainloop()

if __name__ == "__main__":
    main()