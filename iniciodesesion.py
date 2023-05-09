from tkinter import StringVar, Entry, Label, Button, Tk, messagebox as tk
from PIL import Image, ImageTk
from formularioarticulos import FormularioArticulos

class Login:
    def __init__(self):
        
        self.root = Tk()
        self.root.title("Inicio de sesión")
        self.root.geometry("400x400")
        self.root.resizable(False, False)

        # Encabezado con título y imagen
        encabezado = Label(self.root, text="¡Bienvenido!", font=("Arial", 20))
        encabezado.pack(pady=20)
        imagen = Image.open("imagen_inicio_sesion.png")
        imagen = imagen.resize((80,80), Image.ANTIALIAS)
        imagen = ImageTk.PhotoImage(imagen)
        lbl_imagen = Label(self.root, image=imagen)
        lbl_imagen.image = imagen  # evitar que la imagen sea destruida por el recolector de basura
        lbl_imagen.pack(pady=10)

        # Variables para almacenar los valores de entrada del usuario y la contraseña
        self.usuario = StringVar()
        self.contraseña = StringVar()

        # Etiquetas y campos de entrada para el usuario y la contraseña
        lbl_usuario = Label(self.root, text="Usuario:", font=("Arial", 14))
        lbl_usuario.pack(pady=5)
        ent_usuario = Entry(self.root, textvariable=self.usuario, font=("Arial", 14))
        ent_usuario.pack(pady=5)

        lbl_contraseña = Label(self.root, text="Contraseña:", font=("Arial", 14))
        lbl_contraseña.pack(pady=5)
        ent_contraseña = Entry(self.root, textvariable=self.contraseña, show="*", font=("Arial", 14))
        ent_contraseña.pack(pady=5)

        # Botón de inicio de sesión
        btn_ingresar = Button(self.root, text="Ingresar", font=("Arial", 14), command=self.verificar_login, bg="#4CAF50", fg="white", activebackground="#36743C", activeforeground="white")
        btn_ingresar.pack(pady=10)

    # Método para verificar el inicio de sesión
    def verificar_login(self):
        usuario = self.usuario.get()
        contraseña = self.contraseña.get()
        
        # Verifica que el usuario y la contraseña sean correctos
        if (usuario.lower() == "admin" and contraseña.lower() == "1234"):
            tk.showinfo("Inicio de sesión", "Inicio de sesión exitoso.")
            self.root.destroy()
            formulario = FormularioArticulos() # crear ventana principal
           
        else:
            tk.showerror("Inicio de sesión", "Usuario o contraseña incorrectos.")
            
        
    def mainloop(self):
        self.root.mainloop()
