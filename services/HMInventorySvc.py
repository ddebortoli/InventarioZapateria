
class HMInventory():
    def __init__(self,name=None,mark='',price='',amount='',operation=''):
        self.name = name
        self.mark = mark
        self.price = price
        self.amount = amount
        self.operation = operation
        self.lista = {'NombreZapato':name,
                 'Marca':mark,
                 'Precio':price,
                 'Cantidad':amount
                 }
        
    def selectOperation(self):
        "Function that executes an operation based on the request received"
        operation = self.operation
        if operation == 'ADD_ITEM':
            return self.ADD_ITEM()
        elif operation == 'GET_ITEMS':
            return self.GET_ITEMS()
        elif operation == 'DELETE_ITEM':
            return self.DELETE_ITEM()
        else:
            return print("Invalid or misspelled operation")
        
    def ADD_ITEM(self):
        "Function that validates the entered data and builds the query based on the number of parameters"
        datos = (str(self.name),str(self.mark),str(self.price),str(self.amount))
        try:
            self.error = 'Precio'
            int(self.price)
            self.error = 'Cantidad'
            int(self.amount)
        except:
            print(self.error + " must be integer type")
            return False
        query = "INSERT INTO Articulos(NombreZapato,Marca,Precio,Cantidad)VALUES" + str(datos)
        print(query)
        return query or False

    def GET_ITEMS(self):
        "Function that validates the data and generates the query to enter an article to the database"
        query = "SELECT * FROM Articulos WHERE Id NOT NULL"
        for clave in self.lista:
            if self.lista[clave] not in ['None',None,''] :
                try:
                    query = query + " AND " + str(clave) + " = '" + str(self.lista[clave] + "'")
                except:
                    print("Error on:" + query) 
        return query or False
    
    def DELETE_ITEM(self):
        "Function that validates the data and prepares a query to delete an item"
        query = "DELETE FROM Articulos WHERE Id NOT NULL"
        if len(self.name) < 1:
            print("Name is a mandatory parameter for this operation!")
            return False
        for clave in self.lista:
            if self.lista[clave] not in ['None',None,''] :
                try:
                    query = query + " AND " + str(clave) + " = '" + str(self.lista[clave] + "'")
                except:
                    print("Error on:" + query) 
        return query or False