from tkinter import *
import sqlite3
from tkinter import messagebox


class logInScreen(Tk):
    "LogIn class"
    def __init__(self):
        Tk.__init__(self)
        self.access = ''
        self.logged = False

        self.title('Pantalla de inicio de sesion')
        self.geometry('320x240')

        #Variables for logIn
        self.user = StringVar()
        self.password = StringVar()
        
        #labels and input
        messageUser = Label(self,text="Ingrese su usuario:").place(x=10,y=10)
        boxUser = Entry(self,textvariable=self.user).place(x=150,y=10)
        messagePassword = Label(self,text="Ingrese su contraseña:").place(x=10,y=50)
        boxPassword = Entry(self,textvariable=self.password).place(x=150,y=50)
              
        buttonLogIn = Button(self,text = 'Iniciar sesion',command=self.logInToDB).place(x=120,y=100)
        
        self.mainloop()
        
    def logInToDB(self):
        "Funcion que comprueba si los datos del usuario son correctos"
        try:
            conexion=sqlite3.connect("inventarioHM.db")
            getAccess = conexion.execute("select accessLevel from users where user = ? AND password = ?",(self.user.get(),self.password.get()))
            self.access=getAccess.fetchone()
            conexion.close()
            if self.access != None:
                self.logged = True
                self.destroy()   
            else:
                messagebox.showinfo("Credenciales invalidas","Usuario o contraseña incorrecta, compruebe sus datos y vuelva a intentarlo")
        except:
            print("Fallo al conectarse a la base de datos") 
    
class App2(Tk):
    def __init__(self,accessLevel):
        Tk.__init__(self)

        self.title('Pantalla de inicio')
        self.geometry('320x240')
        
        self.addItem = Button(self,text="Agregar articulo",command=self.addItemView,padx=10)
        self.addItem.place(x=20,y=10)
                
        self.checkItems = Button(self,text="Obtener listado",padx=10)
        self.checkItems.place(x=20,y=60)
        
        self.deleteItem = Button(self,text="Borrar un producto",padx=10)
        self.deleteItem.place(x=20,y=110)

        self.addSale = Button(self,text="Registrar venta",padx=10)
        self.addSale.place(x=20,y=160)  
        
        self.showViews(accessLevel)
        
        self.mainloop()

    def showViews(self,accessLevel):
        "Funcion que elimina las opciones en base al nivel de acceso del usuario"
        if accessLevel[0] == 2 or accessLevel[0] == 3:
            self.addItem = self.addItem.destroy()
            self.deleteItem = self.deleteItem.destroy()
        elif accessLevel[0] == 3:
            self.addSale = self.addSale.destroy()


    def insertNewItem(self,zapato,marca,precio,cantidad):
        try:
            conexion=sqlite3.connect("inventarioHM.db")
            insertNewItem = conexion.execute("INSERT INTO Articulos (NombreZapato,Marca,Precio,Cantidad) VALUES (?,?,?,?)",(zapato,marca,precio,cantidad))
            messagebox.showinfo("Articulo guardado","Articulo guardado exitosamente!")
        except:
            messagebox.showinfo("Error al guardar","Error al guardar, verifique los datos, si el error persiste contacte a mantenimiento")
    
    def on_entry_validate(self):
        "Funcion que valida los campos enteros"
        numeros = [self.cantidad.get(),self.precio.get()]
        try:
            for i in numeros:
                x = int(i)
        except ValueError:
            messagebox.showinfo("Parametro de entrada invalido", i +" debe ser de tipo numerico")
        else:
            self.insertNewItem(self.zapatilla.get(),self.marca.get(),self.precio.get(),self.cantidad.get())
     
    def addItemView(self):
        "Funcion que abre la ventana de agregar Ventas"
        addItemWindow = Toplevel(self)
        addItemWindow.geometry = ("600x600")
        
        self.zapatilla = StringVar()
        self.marca = StringVar()
        self.precio = StringVar()
        self.cantidad = StringVar()
        
        
        zapatillaLabel = Label(addItemWindow,text="Nombre zapatilla:").place(x=10,y=10)
        zapatillaInput = Entry(addItemWindow,textvariable=self.zapatilla).place(x=150,y=10)
        
        marcaLabel = Label(addItemWindow,text="Ingrese marca:").place(x=10,y=50)
        marcaInput = Entry(addItemWindow,textvariable=self.marca).place(x=150,y=50)
    
    
        precioLabel = Label(addItemWindow,text="Ingrese precio:").place(x=10,y=110)
        precioInput = Entry(addItemWindow,textvariable=self.precio).place(x=150,y=110)
        
        cantidadLabel = Label(addItemWindow,text="Ingrese cantidad:").place(x=10,y=150)
        cantidadInput = Entry(addItemWindow,textvariable=self.cantidad).place(x=150,y=150)
              
        buttonLogIn = Button(addItemWindow,text = 'Registrar producto',command=self.on_entry_validate).place(x=120,y=200)
        

    def checkItemsView(self):
        pass
    def deleteItemView(self):
        pass
    def addSaleView(self):
        pass
    
if __name__ == '__main__':

    app1 = logInScreen()

    if app1.logged:
        App2(app1.access)