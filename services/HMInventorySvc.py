
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
        operation = self.operation
        if operation == 'AGREGAR_ARTICULO':
            return self.AGREGAR_ARTICULO()
        elif operation == 'OBTENER_ARTICULOS':
            return self.OBTENER_ARTICULOS()
        elif operation == 'ELIMINAR_ARTICULOS':
            return self.ELIMINAR_ARTICULOS()
        else:
            return print("La operacion enviada es invalida")
        #Prueba
    def AGREGAR_ARTICULO(self):
        datos = (str(self.name),str(self.mark),str(self.price),str(self.amount))
        try:
            self.error = 'Precio'
            int(self.price)
            self.error = 'Cantidad'
            int(self.amount)
        except:
            print(self.error + " debe ser de tipo entero")
            return False
        query = "INSERT INTO Articulos(NombreZapato,Marca,Precio,Cantidad)VALUES" + str(datos)
        print(query)
        return query or False

    def OBTENER_ARTICULOS(self):
        query = "SELECT * FROM Articulos WHERE Id NOT NULL"
        for clave in self.lista:
            if self.lista[clave] not in ['None',None,''] :
                try:
                    query = query + " AND " + str(clave) + " = '" + str(self.lista[clave] + "'")
                except:
                    print("Error en:" + query) 
        return query or False
    def ELIMINAR_ARTICULOS(self):
        query = "DELETE FROM Articulos WHERE Id NOT NULL"
        if len(self.name) < 1:
            print("El nombre del zapato es obligatorio para esta operacion!")
            return False
        for clave in self.lista:
            if self.lista[clave] not in ['None',None,''] :
                try:
                    query = query + " AND " + str(clave) + " = '" + str(self.lista[clave] + "'")
                except:
                    print("Error en:" + query) 
        return query or False
    
#HMInventory(None,None,None,'1500','OBTENER_ARTICULOS').selectOperation()