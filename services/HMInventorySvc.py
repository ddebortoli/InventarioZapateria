
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
        elif operation == 'REGISTRAR_VENTA':
            return self.REGISTRAR_VENTA()
        
    def AGREGAR_ARTICULO(self):
        pass
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
        pass
    def REGISTRAR_VENTA(self):
        pass
    
#HMInventory(None,None,None,'1500','OBTENER_ARTICULOS').selectOperation()