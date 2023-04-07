from tkinter import StringVar, Entry, Label, Button, Tk, messagebox as tk



from formularioarticulos import FormularioArticulos


class Login:
    def __init__(self):

        self.root = Tk()
        self.root.title("Inicio de sesión")
        self.root.geometry("400x300")
        self.root.resizable(False, False)

        # Variables para almacenar los valores de entrada del usuario y la contraseña
        self.usuario = StringVar()
        self.contraseña = StringVar()

        # Etiquetas y campos de entrada para el usuario y la contraseña
        lbl_usuario = Label(self.root, text="Usuario: ")
        lbl_usuario.pack()
        ent_usuario = Entry(self.root, textvariable=self.usuario)
        ent_usuario.pack()

        lbl_contraseña = Label(self.root, text="Contraseña: ")
        lbl_contraseña.pack()
        ent_contraseña = Entry(self.root, textvariable=self.contraseña, show="*")
        ent_contraseña.pack()

        # Botón de inicio de sesión
        btn_ingresar = Button(self.root, text="Ingresar", command=self.verificar_login)
        btn_ingresar.pack()


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
        