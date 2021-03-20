import repositories.executeQuery as DB
import services.HMInventorySvc as Op

class mainOperations():
    def __init__(self,name='',mark='',price='',amount='',operation=''):
        self.name = name
        self.mark = mark
        self.price = price
        self.amount = amount
        self.operation = operation
        
    def callOperations(self):
        errorValues = ['AGREGAR_ARTICULO','OBTENER_ARTICULOS','ELIMINAR_ARTICULOS','REGISTRAR_VENTA']
        if (self.operation).upper in errorValues:
            print("Debe seleccionar una operacion valida")
        else:
            query = Op.HMInventory(self.name,self.mark,self.price,self.amount,self.operation).selectOperation()
            if query:
                result = DB.execQuery(query).executeQuery()
                return result

print(mainOperations(None,None,'1000','1600','OBTENER_ARTICULOS').callOperations())