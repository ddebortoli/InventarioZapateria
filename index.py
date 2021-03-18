from tkinter import *
import sqlite3
from tkinter import messagebox
from tkinter import ttk


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
    
class viewScreen(Tk):
    
    def __init__(self,accessLevel):
        Tk.__init__(self)

        self.zapatilla = StringVar()
        self.marca = StringVar()
        self.precio = StringVar()
        self.cantidad = StringVar()
        self.operationName = StringVar()
        
        self.title('Pantalla de inicio')
        self.geometry('500x500')
        
        self.addItem = Button(self,text="Agregar articulo",command=self.addItemView,padx=10)
        self.addItem.place(x=20,y=10)
                
        self.checkItems = Button(self,text="Obtener listado",command=self.checkItemsView, padx=10)
        self.checkItems.place(x=20,y=60)
        
        self.deleteItem = Button(self,text="Borrar un producto",command=self.deleteItemView,padx=10)
        self.deleteItem.place(x=20,y=110)

        self.addSale = Button(self,text="Registrar venta",command=self.addSaleView,padx=10)
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

    def on_entry_validate(self):
        "Funcion que valida los campos enteros"
        numeros = {'Cantidad':self.cantidad.get(),'Precio':self.precio.get()}
        try:
            for campo in numeros:
                x = int(numeros[campo])
        except ValueError:
            messagebox.showinfo("Parametro de entrada invalido", campo +" debe ser de tipo numerico")
        else:
            if (self.operationName == 'addItem'):
                operation = DataBase("",self.zapatilla.get(),self.marca.get(),self.cantidad.get(),self.precio.get()).addItemsToDB()
            elif(self.operationName == 'deleteItem'):
                operation = DataBase("",self.zapatilla.get(),self.marca.get(),self.cantidad.get(),self.precio.get()).deleteItemFromDB()
            elif(self.operationName == 'addSale'):
                operation = DataBase("",self.zapatilla.get(),self.marca.get(),self.precio.get()).addSaleToDB(self.cantidad.get())
                
    def addItemView(self):
        "Funcion que abre la ventana de agregar Ventas"
        addItemWindow = Toplevel(self)
        addItemWindow.title("Agregar articulo")
        
        zapatillaLabel = Label(addItemWindow,text="Nombre zapatilla:").grid(row=0,column=0)
        zapatillaInput = Entry(addItemWindow,textvariable=self.zapatilla).grid(row = 0,column=1)
        
        marcaLabel = Label(addItemWindow,text="Ingrese marca:").grid(row=1,column=0)
        marcaInput = Entry(addItemWindow,textvariable=self.marca).grid(row=1,column=1)
    
        precioLabel = Label(addItemWindow,text="Ingrese precio:").grid(row=2,column=0)
        precioInput = Entry(addItemWindow,textvariable=self.precio).grid(row=2,column=1)
        
        cantidadLabel = Label(addItemWindow,text="Ingrese cantidad:").grid(row=3,column=0)
        cantidadInput = Entry(addItemWindow,textvariable=self.cantidad).grid(row=3,column=1)
        
        self.operationName = 'addItem'
        buttonLogIn = Button(addItemWindow,text ='Registrar producto',command=self.on_entry_validate).grid(row=5 ,column=1)
       
    def checkItemsView(self):
        "Funcion que devuelve un listado de articulos"
        checkItemWidow = Toplevel(self)
        checkItemWidow.title("Listado de articulos")
        
        treeView = ttk.Treeview(checkItemWidow)
        treeView.grid(columnspan=2)
        treeView["columns"] = ["Codigo ART.", "Nombre","Marca","Precio","Costo"]
        treeView["show"] = "headings"
        
        treeView.heading("Codigo ART.", text="Codigo ART.")
        treeView.heading("Nombre", text="Nombre")
        treeView.heading("Marca", text="Marca")
        treeView.heading("Precio", text="Precio")
        treeView.heading("Costo", text="Costo") 
        
        self.zapatilla = 'None'
        self.marca = 'None'
        self.precio = 'None'
        self.cantidad = 'None'
        
        #Mostrar los datos
        tuples = DataBase("",self.zapatilla,self.marca,self.precio,self.cantidad).getItemsFromDB()
        
        index = iid = 0
        for row in tuples:
            treeView.insert("", index, iid, values=row)
            index = iid = index + 1
        
    def deleteItemView(self):
        addItemWindow = Toplevel(self)
        addItemWindow.title("Eliminar articulo")        
        zapatillaLabel = Label(addItemWindow,text="Nombre zapatilla:").grid(row=0,column=0)
        zapatillaInput = Entry(addItemWindow,textvariable=self.zapatilla).grid(row=0,column=1)
        
        marcaLabel = Label(addItemWindow,text="Ingrese marca:").grid(row=1,column=0)
        marcaInput = Entry(addItemWindow,textvariable=self.marca).grid(row=1,column=1)
    
        precioLabel = Label(addItemWindow,text="Ingrese precio:").grid(row=2,column=0)
        precioInput = Entry(addItemWindow,textvariable=self.precio).grid(row=2,column=1)
        
        cantidadLabel = Label(addItemWindow,text="Ingrese cantidad:").grid(row=3,column=0)
        cantidadInput = Entry(addItemWindow,textvariable=self.cantidad).grid(row=3,column=1)
        
        self.operationName = 'deleteItem'      
        buttonLogIn = Button(addItemWindow,text = 'Borrar producto',command=self.on_entry_validate).grid(row=4,column=0)
    
    def addSaleView(self):
        "Funcion que agrega la visual de ventas"
        addItemWindow = Toplevel(self)
        addItemWindow.geometry = ("600x600")
        
        zapatillaLabel = Label(addItemWindow,text="Nombre zapatilla:").place(x=10,y=10)
        zapatillaInput = Entry(addItemWindow,textvariable=self.zapatilla).place(x=150,y=10)
        
        marcaLabel = Label(addItemWindow,text="Ingrese marca:").place(x=10,y=50)
        marcaInput = Entry(addItemWindow,textvariable=self.marca).place(x=150,y=50)
    
        precioLabel = Label(addItemWindow,text="Ingrese precio:").place(x=10,y=110)
        precioInput = Entry(addItemWindow,textvariable=self.precio).place(x=150,y=110)
        
        cantidadLabel = Label(addItemWindow,text="Ingrese cantidad:").place(x=10,y=150)
        cantidadInput = Entry(addItemWindow,textvariable=self.cantidad).place(x=150,y=150)
        
        self.operationName = 'addSale'      
        buttonLogIn = Button(addItemWindow,text = 'Registrar venta',command=self.on_entry_validate).place(x=120,y=200)

class DataBase():
    def __init__(self,code=None,name=None,mark=None,price=None,amount=None):
        self.code = code
        self.name = name
        self.mark = mark
        self.price = price
        self.amount = amount
        self.conexion=sqlite3.connect("inventarioHM.db")
        self.lista = {
            'NombreZapato':str(name),
            'Marca':str(mark),
            'Precio':str(price),
            'Cantidad':str(amount)
            }
            
    def getItemsFromDB(self):
        "Funcion que obtiene registros de la base de datos en base a la cantidad de filtros enviados"
        query = "SELECT * FROM Articulos WHERE Id NOT NULL"
        for clave in self.lista:
            if self.lista[clave] != None and self.lista[clave] != 'None' :
                try:
                    query = query + " AND " + str(clave) + " = '" + str(self.lista[clave] + "'")
                except:
                    print("Error en:" + query)
        
        result = self.conexion.execute(query).fetchall()  
        return result
            
    def addItemsToDB(self):
        "Funcion que inserta registros a la base de datos"
        itemExist = self.getItemsFromDB()
        if itemExist:
            messagebox.showinfo("Error al agregar","Este articulo ya existe en el sistema")
        else:
            query = "INSERT INTO Articulos(NombreZapato,Marca,Precio,Cantidad)VALUES(?,?,?,?)"
            datos = (str(self.name),str(self.mark),self.price,self.amount)
            self.conexion.execute(query,datos)  
            self.conexion.commit() 
            itemExist = self.getItemsFromDB() 
            if itemExist:
                messagebox.showinfo("Exito","Articulo ingresado exitosamente")
            else:
                messagebox.showinfo("Error al agregar","Revise su articulo y vuelva a intentar, si el error persiste contacte con un administrador")

    def addSaleToDB(self,amountOfItem):
        "funcion que resta articulos a la base de datos"
        selectItem = self.getItemsFromDB()
        if selectItem:
            if selectItem[0][4] < int(amountOfItem):
                messagebox.showinfo("Error al actualizar","La cantidad seleccionada es superior al stock vigente")
            else:
                try:
                    query = "UPDATE Articulos SET Cantidad = Cantidad - " + str(amountOfItem)        
                    print(query)
                    self.conexion.execute(query)  
                    self.conexion.commit()
                    messagebox.showinfo("Exito al registrar","La venta se ha realizado exitosamente") 
                except:
                    messagebox.showinfo("Error al actualizar","Contacte con un administrador para mas detalles")
        else:
            messagebox.showinfo("Error al actualizar","El registro ingresado no existe en el stock vigente")
                
    def deleteItemFromDB(self):
        "Funcion que elimina un registro de la base de datos"
        query = "DELETE FROM Articulos WHERE Id NOT NULL"
        cont = 0
        for clave in self.lista:
            if self.lista[clave] != None and self.lista[clave] != 'None':
                try:
                    query = query + " AND " + str(clave) + " = '" + str(self.lista[clave] + "'")
                except:
                    print("Error en:" + query)
            else:
                cont = cont + 1
        if (cont < 4):
            self.conexion.execute(query)  
            self.conexion.commit()
            messagebox.showinfo("Exito al borrar","Articulo borrado exitosamente") 
        else:
            messagebox.showinfo("Error al borrar","Se debe especificar por lo menos un valor")

if __name__ == '__main__':

    app1 = logInScreen()

    if app1.logged:
        viewScreen(app1.access)
    
    DataBase.conexion.close()
        
    #Prueba para obtener datos filtrando por uno o mas campos
    #test1GetDataByFilter = DataBase(None,None,None,None).getItemsFromDB()
    
    #Prueba para intentar insertar datos que ya existen, debe devolver error
    #test2InsertDataThatAlreadyExist = DataBase("","Adidas sport II","Adidas","5000","4").addItemsToDB()
    
    #Prueba para insertar datos que no existen, deben generarse nuevos datos todo el tiempo
    #test3InsertDataThatDoesntExist = DataBase("",'Hight sport','Adidas','1000','19').addItemsToDB()
    
    #Prueba para eliminar datos por filtracion
    #test4deleteFromDB = DataBase("","1","DataAlazar","5000","4").deleteItemFromDB()

    #Prueba para eliminar datos por filtracion, al estar vacio devuelve error
    #test5deleteFromDB = DataBase().deleteItemFromDB()
    
    #Prueba para registrar una venta
    #test6UpdateTable = DataBase("",'New Ballance','New Ballance','1000').addSaleToDB(5)
    