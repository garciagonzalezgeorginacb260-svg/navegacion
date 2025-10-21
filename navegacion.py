import tkinter as tk
from tkinter import ttk

def regresar_ventana1(ventana1, ventana2):
    ventana2.destroy()
    ventana1.deiconify()

def abrir_ventana2(ventana1):
    ventana1.withdraw()
    ventana2 = tk.Toplevel(ventana1)
    ventana2.title("Ventana 2")
    ventana2.geometry("400x300")

    btn_regresar_ventana1 = ttk.Button(
        ventana2,
        text="Regresar a Ventana 1",
        command=lambda: regresar_ventana1(ventana1, ventana2)
    )
    btn_regresar_ventana1.pack(pady=20)

def main():
    ventana1 = tk.Tk()
    ventana1.title("Ventana 1")
    ventana1.geometry("400x300")

    btn_abrir_ventana2 = ttk.Button(
        ventana1,
        text="Abrir Ventana 2",
        command=lambda: abrir_ventana2(ventana1)
    )
    btn_abrir_ventana2.pack(pady=20)

    ventana1.mainloop()

if __name__ == "__main__":
    main()